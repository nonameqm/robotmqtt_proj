import paho.mqtt.client as mqtt
import json
from pydantic.types import Json
from influx_database import *
from post_db import psqlController

influxdb=get_influxdb(db='testdb')
tablename_list=['current', 'voltage', 'status', 'errorcode']
postgresql=psqlController()



class MQTT_Subscriber():
    def __init__(self, name: str, host, port, topic):
        self.client=mqtt.Client(name)
        self.client.connect(host=host, port=port)
        self.client.on_message=on_message
        self.client.on_connect=on_connect
        self.client.subscribe(topic)
        
    def loop_start(self):
        self.client.loop_forever()

def on_message(client, userdata, message):
    json_data=json.loads(str(message.payload.decode("utf-8")))
    topic=message.topic
    print("message topic : ", topic)
    print("message qos : ", message.qos)
    print("message retain flag : ", message.retain)
    # if 'robot_status' in json_data['robot_data'].keys():
    #     print("message received : ", json_data['robot_data'])
    print("message received : ", json_data['robot_data'])
    input_db(topic, influxdb, json_data)
    

def on_connect(client, userdata, flags, rc):
    print("rc : "+ str(rc))


def input_db(topic: str, influxdb : InfluxDBClient, json_data: Json):
    tablename=topic.split('/')[-1]
    robot_data=json_data['robot_data']
    robot_serial=json_data['robot_serial']
    robot_ip=json_data['robot_ip']
    
    if tablename not in tablename_list:
        return 
    
    #influx db
    json_body=[]
    point={}
    point['measurement'] = tablename
    point['tags'] = {
        "robot_serial" : robot_serial,
        "robot_ip" : robot_ip
    }
    point['fields'] = robot_data
    point['time'] = datetime.now()-timedelta(hours=-9)
    json_body.append(point)
    influxdb.write_points(json_body)


    #postgresql
    if tablename in ['status', 'errorcode']:
        for key, value in robot_data.items():
            try:
                robot_update_command="UPDATE robot_data SET rbdata_value=%d where robot_serial=\'%s\' and rbdata_type=\'%s\'"%(value, robot_serial, key)
                postgresql.command_insert(robot_update_command)
                postgresql.db.commit()
            except:
                postgresql.db.rollback()
    




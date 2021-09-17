import paho.mqtt.client as mqtt
import json

robot_status_data={
    "robot_ip" : "192.168.1.62",
    "robot_serial" : 'XI120307201B60',
    "robot_data" : {
        "robot_status" : 2
    }
}

robot_errorcode={
    "robot_ip" : "192.168.1.62",
    "robot_serial" : 'XI120307201B60',
    "robot_data":{
        "error_code" : 2
    }
}

robot_current_data={
    "robot_ip" : "192.168.1.62",
    "robot_serial" : 'XI120307201B60',
    "robot_data" : {
        'robot_current1': 0.30836090445518494, 
        'robot_current2': -2.012941360473633, 
        'robot_current3': -1.9815236330032349, 
        'robot_current4': 0.18996717035770416,
        'robot_current5': -0.042603544890880585,
        'robot_current6': -0.02506146766245365,
    }
}

robot_voltage_data={
    "robot_ip" : "192.168.1.62",
    "robot_serial" : 'XI120307201B60',
    "robot_data" : {
        'robot_voltage1': 23.790000915527344, 
        'robot_voltage2': 23.770000457763672, 
        'robot_voltage3': 23.8799991607666, 
        'robot_voltage4': 23.780000686645508, 
        'robot_voltage5': 23.799999237060547,
        'robot_voltage6': 23.68000030517578    
    }
}





robot_status_data_json=json.dumps(robot_status_data)
robot_current_data_json=json.dumps(robot_current_data)
robot_voltage_data_json=json.dumps(robot_voltage_data)
robot_errorcode_json=json.dumps(robot_errorcode)

mqttc=mqtt.Client("test_publisher")
mqttc.connect("localhost", 1883)
mqttc.publish("real_time/status", robot_status_data_json)
mqttc.publish("real_time/errorcode", robot_errorcode_json)
mqttc.publish("real_time/voltage", robot_voltage_data_json)
mqttc.publish("real_time/current", robot_current_data_json)




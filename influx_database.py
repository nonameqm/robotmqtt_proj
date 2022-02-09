from datetime import datetime, timedelta
import pprint
from influxdb import InfluxDBClient

def get_influxdb(db, host='101.101.218.67', port=8086, user='rcs_admin', passwd='1q2w3e4r!'):
    client=InfluxDBClient(host, port, user, passwd, db)
    try:
        client.create_database(db)
        print('Connection Successful')
        print('=====================')
        print('Connection Info')
        print('=====================')
        print('host : ', host)
        print('Port : ', port)
        print('Username : ', user)
        print('Database : ', db)
    except:
        print('Connection Failed')
        pass
    return client

# def input_data(influxdb: InfluxDBClient, )


def input_test(influxdb : InfluxDBClient):
    json_body=[]
    tablename='error_rate'
    fieldname='error'
    point={
        "measurement" : tablename,
        "tags":{
            "robot_serial" : "000001",
            "og_name" : "tc01_001",
            "company_name" : "tc01"
        },
        "fields":{
            fieldname: 0
        },
        #korean time
        "time": datetime.now()-timedelta(hours=-9)
    }
    json_body.append(point)
    influxdb.write_points(json_body)

    result=influxdb.query('select * from %s'%tablename)
    pprint.pprint(result.raw)

db=get_influxdb(db='robotdata')
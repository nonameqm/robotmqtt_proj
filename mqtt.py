from post_db import psqlController
from fastapi_mqtt import FastMQTT, MQTTConfig

from mqtt_subscribe import *
import json

HOST='0.0.0.0'
PORT=1883
TOPIC="real_time/#"

#Application Configuration


mqtt_data_subscriber=MQTT_Subscriber("robot_data_subscriber", host=HOST, port=PORT, topic=TOPIC)
mqtt_data_subscriber.loop_start()

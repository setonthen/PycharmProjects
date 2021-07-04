import paho.mqtt.publish as publish
import json

publish.single("ii/sensor1/temp","hello", hostname="broker.mqttdashboard.com")  #solution 1

sensorData ={"temperature":20}  #solution2 using dictionary formate
publish.single("ii/sensor1/temp",json.dumps(sensorData), hostname="broker.mqttdashboard.com")  #solution2



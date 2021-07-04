import paho.mqtt.subscribe as subscribe
import json

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))

    recMsg = json.loads(message.payload)
    print ("the sensor temperature is:" + str(recMsg["temperature"]))

subscribe.callback(on_message_print, "ii/sensor1/temp", hostname="broker.mqttdashboard.com")

# after running this code in python. then go to http://www.hivemq.com/demos/websocket-client/ to publish the value
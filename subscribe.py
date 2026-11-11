from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from pyspectator.processor import Cpu

import config


def customCallback(client, userdata, message):
    print("Message received:")
    print(message.payload)
    if message.payload == b'{\n  "temperature"\n}':
        msg = str(cpu.temperature)
        myMQTTClient.publish(config.TOPIC, msg, 0)


myMQTTClient = AWSIoTMQTTClient(config.CLIENT_ID)
cpu = Cpu(monitoring_latency=1)

myMQTTClient.configureEndpoint(config.ENDPOINT, config.PORT)
myMQTTClient.configureCredentials(config.ROOT_CA, config.PRIVATE_KEY, config.CERTIFICATE)

myMQTTClient.connect()
print("Connected")

myMQTTClient.subscribe(config.TOPIC, 1, customCallback)

print("Waiting for messages. Press Enter to stop...")
input()

myMQTTClient.unsubscribe(config.TOPIC)
print("Client unsubscribed")

myMQTTClient.disconnect()
print("Client disconnected")

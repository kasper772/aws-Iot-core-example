from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from pyspectator.processor import Cpu

def customCallback(client,userdata,message):
    print("callback came...")
    print(message.payload)
    if message.payload==b'{\n  "temperature"\n}':
        msg=cpu.temperature
        topic = "general/inbound"
        myMQTTClient.publish(topic, msg, 0) 


myMQTTClient = AWSIoTMQTTClient('333')
cpu = Cpu(monitoring_latency=1)


myMQTTClient.configureEndpoint("endpoint",8883)
myMQTTClient.configureCredentials("./AmazonRootCA1 (2).pem", "./333.private.key","./333.cert.pem")

myMQTTClient.connect()
print("ok")


myMQTTClient.subscribe("general/inbound", 1, customCallback)

print('waiting for the callback. Click to continue...')

y=input()
myMQTTClient.unsubscribe("general/inbound")
print("Client unsubscribed") 


myMQTTClient.disconnect()
print("Client Disconnected")
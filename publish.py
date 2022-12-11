from AWSIoTPythonSDK.MQTTLib  import AWSIoTMQTTClient

myMQTTClient=AWSIoTMQTTClient('333')


myMQTTClient.configureEndpoint("endpoint",8883)
myMQTTClient.configureCredentials("./AmazonRootCA1 (2).pem", "./333.private.key","./333.cert.pem")

myMQTTClient.connect()
print("ok")
# topic =
msg="Sample data from the device"
topic = "general/inbound"
myMQTTClient.publish(topic, msg, 0)  
print("Message Sent")


myMQTTClient.disconnect()
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

import config

myMQTTClient = AWSIoTMQTTClient(config.CLIENT_ID)
myMQTTClient.configureEndpoint(config.ENDPOINT, config.PORT)
myMQTTClient.configureCredentials(config.ROOT_CA, config.PRIVATE_KEY, config.CERTIFICATE)

myMQTTClient.connect()
print("Connected")

msg = "Sample data from the device"
myMQTTClient.publish(config.TOPIC, msg, 0)
print("Message sent")

myMQTTClient.disconnect()

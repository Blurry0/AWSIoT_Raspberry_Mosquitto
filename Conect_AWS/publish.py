import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


myMQTTClient = AWSIoTMQTTClient('Prueba') #Genera una llave aleatoria


Root_CA = "./Certificates/root-ca.pem"
Private_Key = "./Certificates/private.pem.key"
Certificate = "./Certificates/certificate.pem.crt"

myMQTTClient.configureEndpoint("a21g05mm980mir-ats.iot.us-east-2.amazonaws.com", 8883)

myMQTTClient.configureCredentials(Root_CA, Private_Key, Certificate)

myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5) # 5 sec
print ('Initiating Realtime Data Transfer From Raspberry Pi...')
myMQTTClient.connect()

print("Publishing Message From Raspberry Pi")
myMQTTClient.publish(
    topic="home/helloworld",
    QoS = 1,
    payload='{"Message":"Message From Raspberry Pi"}'
)
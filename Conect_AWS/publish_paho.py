import paho.mqtt.client as paho
import os
import socket
import ssl
import json


mqttc = paho.Client()

awshost = "a21g05mm980mir-ats.iot.us-east-2.amazonaws.com"
topic = "home/helloworld"
awsport = 8883
clientId = "Prueba"
caPath = "./Certificates/root-ca.pem"
certPath = "./Certificates/certificate.pem.crt"
keyPath = "./Certificates/private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.publish(topic,payload='{"message":"Message from Raspberry Pi"}', qos=1)
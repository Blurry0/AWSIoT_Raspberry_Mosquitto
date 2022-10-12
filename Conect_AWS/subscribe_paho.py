import paho.mqtt.client as paho
import os
import socket
import ssl
import json

def on_connect(client, userdata, flags, rc):
    print("Connected to AWS IoT")
    print("Subscribing to topic...")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)


def on_message(client, userdata, msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8"))
    m_in=json.loads(m_decode) #decode json data
    print("message = ",m_in["message"])


mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

awshost = "a21g05mm980mir-ats.iot.us-east-2.amazonaws.com"
topic = "home/helloworld"
awsport = 8883
clientId = "Prueba"
caPath = "./Certificates/root-ca.pem"
certPath = "./Certificates/certificate.pem.crt"
keyPath = "./Certificates/private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_forever()
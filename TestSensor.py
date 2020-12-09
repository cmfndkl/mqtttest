from decimal import Decimal
import RPi.GPIO as GPIO
import math
import requests
from time import sleep
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(3, GPIO.IN)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial=GPIO.HIGH)

myMQTTClient = AWSIoTMQTTClient("Test") #random key
myMQTTClient.configureEndpoint("a78cdcu1pkqzx-ats.iot.us-east-2.amazonaws.com", 8883)

myMQTTClient.configureCredentials("/home/pi/AWSIoT/root-ca.pem", "/home/pi/AWSIoT/private.pem.key", "/home/pi/AWSIoT/certificate.pem.crt")

myMQTTClient.configureOfflinePublishQueueing(-1)
myMQTTClient.configureDrainingFrequency(2)
myMQTTClient.configureConnectDisconnectTimeout(10)
myMQTTClient.configureMQTTOperationTimeout(5)
print("Demo...")
myMQTTClient.connect()

while True:
    val = GPIO.input(3)
    
    if val == 0:
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        myMQTTClient.publish(
            topic="home/helloworld",
            QoS=1,
            payload="{'Message':'Dolu'}")
        sleep(20)
    else: 
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(8, GPIO.LOW)
        myMQTTClient.publish(
            topic="home/helloworld",
            QoS=1,
            payload="{'Durum':'Boş'}")
        sleep(20)
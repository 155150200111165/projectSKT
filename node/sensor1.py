#!/usr/bin/python
import sys
import Adafruit_DHT
import paho.mqtt.client as mqtt
import threading, json
from datetime import datetime

#====================================================
# MQTT Settings 
MQTT_Topic_Humidity = "Home/BedRoom/DHT11/Humidity"
MQTT_Topic_Temperature = "Home/BedRoom/DHT11/Temperature"

#====================================================

def on_publish(client, userdata, mid):
    pass
		
mqttc = mqtt.Client()
mqttc.connect = ("10.36.2.251", 1883)
mqttc.on_publish = on_publish
		
def publish_To_Topic(topic, message):
    mqttc.publish(topic,message)

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print 'Temp: {} C; Humidity: {} %;'.format(temperature, humidity)

    #Masukkan data kelembapan
    Humidity_Data = {}
    Humidity_Data['Sensor_ID'] = "Data-1"
    Humidity_Data['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
    Humidity_Data['Humidity'] = humidity
    humidity_json_data = json.dumps(Humidity_Data)
    publish_To_Topic (MQTT_Topic_Humidity, humidity_json_data)

    #Masukkan data temperatur
    Temperature_Data = {}
    Temperature_Data['Sensor_ID'] = "Data-2"
    Temperature_Data['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
    Temperature_Data['Temperature'] = temperature
    temperature_json_data = json.dumps(Temperature_Data)
    publish_To_Topic (MQTT_Topic_Temperature, temperature_json_data)



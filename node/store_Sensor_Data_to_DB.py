import json
import cql

conn = cql.connect(host="127.0.0.1", port=9160, keyspace="sensordb", cql_version='5.0.1')

cur=conn.cursor()

#===============================================================
# Functions to push Sensor Data into Database

# Function to save Temperature to DB Table
def DHT11_Temp_Data_Handler(jsonData):
    #Parse Data 
    json_Dict = json.loads(jsonData)
    SensorID = json_Dict['Sensor_ID']
    Data_and_Time = json_Dict['Date']
    Temperature = json_Dict['Temperature']
	
    #Push into DB Table
    cur.execute("insert into temperature (SensorID, Date_n_Time, Temperature) VALUES ('SensorID','Data_and_Time','Temperature')")
    cur.close()
    print "Inserted Temperature Data into Database."
    print ""

# Function to save Humidity to DB Table
def DHT11_Humidity_Data_Handler(jsonData):
    #Parse Data 
    json_Dict = json.loads(jsonData)
    SensorID = json_Dict['Sensor_ID']
    Data_and_Time = json_Dict['Date']
    Humidity = json_Dict['Humidity']
	
    #Push into DB Table
    cur.execute("insert into humidity (SensorID, Date_n_Time, Humidity) VALUES ('SensorID','Data_and_Time','Humidity')")
    cur.close()
    print "Inserted Humidity Data into Database."
    print ""


#===============================================================
# Master Function to Select DB Funtion based on MQTT Topic

def sensor_Data_Handler(Topic, jsonData):
    if Topic == "Home/BedRoom/DHT11/Temperature":
        DHT11_Temp_Data_Handler(jsonData)
    elif Topic == "Home/BedRoom/DHT11/Humidity":
        DHT11_Humidity_Data_Handler(jsonData)	

#===============================================================
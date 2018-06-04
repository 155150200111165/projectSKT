from flask import Flask, request
from flask_restful import Resource, Api
import time

conn = cql.connect('ip', 9160, keyspace = 'sensordb', user='username', password='password', cql_version='5.0.1')

app = Flask(__name__)
api = Api(app)


class Temperature(Resource):
    def get(self):
        conn = cql.connect()  # connect to database
        query = conn.execute("select * from temperature order by id desc limit 1")  # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]}  # Fetches first column that is Temperature ID

class Humidity(Resource):
    def get(self):
        conn = cql.connect()  # connect to database
        query = conn.execute("select * from humidity order by id desc limit 1")  # This line performs query and returns json result
        return {'humidity': [i[0] for i in query.cursor.fetchall()]}  # Fetches first column that is Humidity ID


api.add_resource(Temperature, '/tempertature')  # Route_1
api.add_resource(Humidity, '/humidity')  # Route_1


if __name__ == '__main__':
    while True :
        app.run(port='5002')
        time.sleep(60)
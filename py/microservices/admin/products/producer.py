import pika, json
from decouple import config

params = pika.URLParameters(config('AMQP'))
connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    property = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=property)
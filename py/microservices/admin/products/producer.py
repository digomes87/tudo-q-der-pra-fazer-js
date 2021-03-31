import pika
from decouple import config, Csv

params = pika.URLParameters(config('AMQP'))
connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='deu tudo certo outra vez')
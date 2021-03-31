import pika
from decouple import config

params = pika.URLParameters(config('AMQP'))
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Okey, all was received')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback)

print('Starting consume')

channel.start_consuming()

channel.close()
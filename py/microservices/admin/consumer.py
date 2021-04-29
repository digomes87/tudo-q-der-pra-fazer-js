import pika, json
from decouple import config, Csv
from products.models import Product

params = pika.URLParameters(config('AMQP'))
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Okey, all was received')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Starting consume')

channel.start_consuming()

channel.close()
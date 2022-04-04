import pika
import json
from .main import Product, db

params = pika.URLParameters("amqps://aetjcpxc:QSgt171LlDoIFdeCBVn1rKNaI1-OjOo2@rat.rmq2.cloudamqp.com/aetjcpxc")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print("Received in admin")
    data = json.loads(body)
    print(data)
    if properties.content_type == "product_created":
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()

channel.close()
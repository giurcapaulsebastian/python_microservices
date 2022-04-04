import pika

params = pika.URLParameters("amqps://aetjcpxc:QSgt171LlDoIFdeCBVn1rKNaI1-OjOo2@rat.rmq2.cloudamqp.com/aetjcpxc")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print("Received in admin")
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()

channel.close()
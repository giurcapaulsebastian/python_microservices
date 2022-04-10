# amqps://aetjcpxc:QSgt171LlDoIFdeCBVn1rKNaI1-OjOo2@rat.rmq2.cloudamqp.com/aetjcpxc
import pika, json

params = pika.URLParameters("amqps://aetjcpxc:QSgt171LlDoIFdeCBVn1rKNaI1-OjOo2@rat.rmq2.cloudamqp.com/aetjcpxc")

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method,body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello', durable=True)


def callback(ch, method, properties, body):
	print(" [x] Received %r" % body)
	time.sleep(body.count(b'.'))
	print( " [x] Done")
	ch.basic_ack(delivery_tag = method.delivery_tag)

# consumer function
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='hello')

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

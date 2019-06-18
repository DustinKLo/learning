#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

# result.method.queue contains a random queue name (ex. amq.gen-JzTY20BRgKO-HjmUJj0wLg)
result = channel.queue_declare(exclusive=True) # deletes queue
queue_name = result.method.queue

# binding the exchange to the queues
channel.queue_bind(exchange='logs',
				  queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
	print(" [x] %r \t queue name: %r" % (body, queue_name))

channel.basic_consume(callback,
					  queue=queue_name,
					  no_ack=True)

channel.start_consuming()

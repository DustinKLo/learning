#!/usr/bin/env python
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')


# result.method.queue contains a random queue name (ex. amq.gen-JzTY20BRgKO-HjmUJj0wLg)
result = channel.queue_declare(exclusive=True) # deletes queue
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

# binding the exchange to the queues
for severity in severities:
	# severity: INFO, WARNING, ERROR
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print(" [*] Waiting for logs. To exit press CRTL+C")

def callback(ch, method, properties, body):
	print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()


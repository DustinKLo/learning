import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
# rabbitmq producer

for i in range(0, 25):
	channel.basic_publish(exchange='', 
						  routing_key='hello', 
						  body='message {}'.format(i))
	print(" [x] sent message '{}!'".format(i))

connection.close()

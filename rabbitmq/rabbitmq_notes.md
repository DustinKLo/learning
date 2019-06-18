# install on mac
`brew install rabbitmq`
`export PATH=$PATH:/usr/local/sbin`

# run rabbitmq server
`rabbitmq-server`
`rabbitmq-server -detached`
`sudo rabbitmqctl stop`

# lists all queues and messages per queue
`sudo rabbitmqctl list_queues`

# creating a user for rabbitmq (not needed for demo learning)
`sudo rabbitmqctl add_user myuser mypassword`
`sudo rabbitmqctl add_vhost myvhost`
`sudo rabbitmqctl set_user_tags myuser mytag`
`sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"`


- WORK QUEUES will distribute time-consuming tasks among multiple workers
	- work queues avoid doing a resource-intensive task immediately and having to wait for it to complete
	- Instead we schedule the task to be done later
	- encapsulate a task as a message and send it to the queue
	- worker process running in the background will pop the tasks and eventually execute the job
	- An ack(nowledgement) is sent back by the consumer to tell RabbitMQ that a particular message had been received, processed and that RabbitMQ is free to delete it.



sudo rabbitmqctl list_queues name messages_ready messages_unacknowledged
durable queue make RabbitMQ will never lose our queue
	- `channel.queue_declare(queue='task_queue', durable=True)`

rabbitmq blindly dispatches every n-th message to the n-th consumer
	- `channel.basic_qos(prefetch_count=1)` prevents that


# lists all exchanges
`sudo rabbitmqctl list_exchanges`
`rabbitmqctl list_bindings` # lists bindings


# Exchanges
- producer sends messages to exchange
 	- exchanges then pus message to queue
- queue is buffer that store messages
- consumer receives messages
- producer -> exchange -> queues
 	- fanout exchange pushes one message to all queues
- exchange types: `direct`, `topic`, `headers` and `fanout`
- `result = channel.queue_declare(exclusive=True)`
	- `exclusive=True` will delete queue when connection is closed
	- will have a randomized queue name


# Routing Keys
- queue binds can take a `routing_key` parameter
- `direct` exchange message goes to the queues whose `binding_key` exactly matches the `routing_key` of the message









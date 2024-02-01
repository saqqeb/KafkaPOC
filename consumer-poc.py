from kafka import KafkaConsumer
from os import getenv

# Kafka Consumer configuration
consumer_config = {
	'bootstrap_servers': getenv('KAFKA_BOOTSTRAP_SERVERS'),
	'sasl_mechanism': 'SCRAM-SHA-256',
	'security_protocol': 'SASL_SSL',
	'sasl_plain_username': getenv('KAFKA_SASL_PLAIN_USERNAME'),
	'sasl_plain_password': getenv('KAFKA_SASL_PLAIN_PASSWORD'),
	'group_id': 'your-consumer-group',  # Replace with your consumer group
	'auto_offset_reset': 'earliest'
}

# Create a standard Kafka Consumer
consumer = KafkaConsumer(
	'test',
	**consumer_config
)

# Consume messages
try:
	for message in consumer:
		print(f"Received message: {message.value}")
except KeyboardInterrupt:
	pass
finally:
	consumer.close()

#
# message.topic,
# 			message.partition,
# 			message.offset,
# 			message.key,
# 			message.value

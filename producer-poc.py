from os import getenv
from kafka import KafkaProducer

# Kafka Producer configuration
producer_config = {
	'bootstrap_servers': getenv('KAFKA_BOOTSTRAP_SERVERS'),
	'sasl_mechanism': 'SCRAM-SHA-256',
	'security_protocol': 'SASL_SSL',
	'sasl_plain_username': getenv('KAFKA_SASL_PLAIN_USERNAME'),
	'sasl_plain_password': getenv('KAFKA_SASL_PLAIN_PASSWORD'),
}

# Create a standard Kafka Producer
producer = KafkaProducer(**producer_config)

# Produce a message
try:
	producer.send('test', b'Your message here')
	producer.flush()
	print("Message produced without Avro schema!")
except Exception as e:
	print(f"Error producing message: {e}")
finally:
	producer.close()

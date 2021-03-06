import pika
import sys

credentials = pika.PlainCredentials('usuario', 'senha')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)
print(" [x] Sent %r" % message)
connection.close()
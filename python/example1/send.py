import pika

credentials = pika.PlainCredentials('usuario', 'senha')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Novo HelloW')

print(' [x] Sent Novo HelloW')

connection.close()
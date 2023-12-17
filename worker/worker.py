import pika

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue='qusai_data', durable=True)

    print("Waiting for messages...")

    def callback(ch, method, properties, body):
        print(f"Received message: {body.decode()}")
        print("Done")

        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='qusai_data', on_message_callback=callback)
    channel.start_consuming()

except pika.exceptions.AMQPConnectionError as exc:
    print(f"Failed to connect to RabbitMQ service: {exc}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

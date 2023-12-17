from flask import Flask
import pika


app = Flask(__name__)

@app.route('/<msg>')
def data(msg):
    try: 
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    except:
        print("Could not connect to rabbitmq...")
        return

    channel = connection.channel()
    channel.queue_declare(queue='qusai_data', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='qusai_data',
        body=msg,
        properties=pika.BasicProperties(
            delivery_mode=2,
        )
    )
    connection.close()
    return f"Sent: {msg} through RabbitMQ"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
    
    
        
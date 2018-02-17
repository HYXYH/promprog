import pika
import os
import time
import sys


def send_test():
    for i in range(10):
        data = 'test {}'.format(i)
        channel.basic_publish(exchange='', routing_key='hello', body=data, properties=pika.BasicProperties(content_type='text/plain', delivery_mode=1))
        time.sleep(1)
    print("All data sent.")


def main():

    print("started! waiting for rabbit...")
    time.sleep( 17 )
    for i in range(3,0,-1):
        print(i)
        time.sleep( 1 )

    connection = pika.BlockingConnection(  pika.URLParameters("amqp://guest:guest@rabbit:5672") )
    print("Connected! Starting transmission.")
    # connection = pika.BlockingConnection(  pika.URLParameters("amqp://guest:guest@localhost:8085") )
    channel = connection.channel() 
    channel.queue_declare(queue='hello') 

    if len(sys.argv) == 1:
        send_test()
    elif len(sys.argv) > 1:
        channel.basic_publish(exchange='', routing_key='hello', body=sys.argv[1], properties=pika.BasicProperties(content_type='text/plain', delivery_mode=1))
    connection.close()




if __name__ == '__main__':
    main()
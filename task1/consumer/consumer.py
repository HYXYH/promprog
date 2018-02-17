import pika
import os
import time
import psycopg2


def main():
    print("started! Waiting for db and rabbit...")
    time.sleep( 10 )
    for i in range(5,0,-1):
        print(i)
        time.sleep( 1 )


    # conn = psycopg2.connect(dbname="task1", user="task1", password="thepass", host="localhost" , port="8081") 
    conn = psycopg2.connect(dbname="task1", user="task1", password="thepass", host="db") 
    db = conn.cursor()
    db.execute("CREATE TABLE messages (id SERIAL PRIMARY KEY, message CHAR(64))")

    connection = pika.BlockingConnection(  pika.URLParameters("amqp://guest:guest@rabbit:5672") )
    # connection = pika.BlockingConnection(  pika.URLParameters("amqp://guest:guest@localhost:8085") )

    print("Connected! Waiting for data.")
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    def callback(ch, method, properties, body):
        recieved = (body.decode())
        print(recieved)
        db.execute("INSERT INTO messages (message) VALUES ('" + recieved + "')")
        conn.commit()

    channel.basic_consume(callback, queue='hello', no_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    main()
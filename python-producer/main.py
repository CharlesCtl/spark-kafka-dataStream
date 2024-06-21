from kafka import KafkaProducer
from kafka.errors import KafkaError
import time

if __name__=="__main__":
    time.sleep(10)
    print("Hello from python container")
    producer = KafkaProducer(bootstrap_servers=['kafka-server-2:9092'])
    if producer.bootstrap_connected():
        for _ in range(2):
            message = b'Hello, Kafka!'
            producer.send('test', message)
    else:
        print('Failed connection')
    producer.close()    
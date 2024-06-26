from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import time
import threading

def init_producer():
    time.sleep(10)
    return KafkaProducer(bootstrap_servers=['kafka-server-2:9092'],
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
def send_message(topic,file,key=None):
    count = 0
    for invoice in read_json(file):
        message = {key: invoice}
        producer.send(topic,message)
        producer.flush()
        count += 1
        if count == 10:
            break
    return True
def read_json(file_path):
    with open(file_path,'r') as file:
        for line in file:
            yield json.loads(line)

file1 = 'invoices_data/invoices-1.json'
file2 = 'invoices_data/invoices-2.json'
topic = 'test'
if __name__=="__main__":
    producer = init_producer()
    if producer.bootstrap_connected():
        thread1 = threading.Thread(target=send_message,args=(topic,file1,1,))
        thread2 = threading.Thread(target=send_message,args=(topic,file2,2,))
        thread1.start()
        thread2.start()
        thread1.join()
        thread1.join()
        producer.close()
    else:
        print('Failed connection')

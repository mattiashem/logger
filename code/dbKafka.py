from kafka import KafkaProducer
from time import sleep
from json import dumps
import os

kafka_servers=str(os.environ.get('KAFKA', 'redpanda:9092'))
kafka_tls=str(os.environ.get('KAFKA_TLS', "none"))
kafka_topic=str(os.environ.get('KAFKA_TOPIC', "events"))
print("Connect to kafka servers: ", kafka_servers)
#if kafka_tls == "none":
producer = KafkaProducer(bootstrap_servers=kafka_servers,
                        value_serializer=lambda x: 
                        dumps(x).encode('utf-8'))
#else:
#    producer = KafkaProducer(bootstrap_servers=kafka_servers,
#                            security_protocol="SSL",
#                            ssl_check_hostname=False,
#                            ssl_cafile='/tls/ca.crt',
#                             value_serializer=lambda x: 
#                             dumps(x).encode('utf-8'))


def addToKafka(data):
    print("Adding data to kafka")
    kafkaRespons= producer.send(kafka_topic, value=data)
    #print(kafkaRespons)


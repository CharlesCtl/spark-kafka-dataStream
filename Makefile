list-topics:
	docker run -it --rm --network spark-kafka-datastream_app-tier bitnami/kafka:latest kafka-topics.sh --list  --bootstrap-server kafka-server-2:9092
create-topic:
	docker run -it --rm --network spark-kafka-datastream_app-tier bitnami/kafka:latest kafka-topics.sh --create --topic test --partitions 1 --replication-factor 1 --bootstrap-server kafka-server-2:9092
write-data:
	docker run -it --rm --network spark-kafka-datastream_app-tier bitnami/kafka:latest kafka-console-producer.sh --topic test --bootstrap-server kafka-server-2:9092
read-data:
	docker run -it --rm --network spark-kafka-datastream_app-tier bitnami/kafka:latest kafka-console-consumer.sh --topic test --from-beginning --bootstrap-server kafka-server-2:9092
run-python-producer:
	docker run -it --rm --name pythonProducer --network spark-kafka-datastream_app-tier charles/python-kafka-producer
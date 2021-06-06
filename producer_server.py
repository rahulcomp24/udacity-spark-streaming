from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):
    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    def generate_data(self):
        with open(self.input_file) as f:
            items = json.load(f)
            for line in items:
                message = self.dict_to_binary(line)
                print(line["crime_id"].encode("utf-8"))
                print(message)
                print(self.topic)
                self.send(
                    self.topic, key=line["crime_id"].encode("utf-8"), value=message
                )
                time.sleep(0.01)

    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode("utf-8")

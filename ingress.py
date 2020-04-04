from google.cloud import pubsub_v1

topic_name = 'projects/Demo/topics/topic.one'

data = [b'demo one',
        b'demo two',
        b'demo three',
        b'demo four']

publisher = pubsub_v1.PublisherClient()

for message in data:
    publisher.publish(topic_name, message)

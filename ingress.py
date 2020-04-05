from google.cloud import pubsub_v1
import google.auth

credentials, project_id = google.auth.default()


topic_name = 'projects/watchful-net-273116/topics/topic.one'

data = [b'demo one',
        b'demo two',
        b'demo three',
        b'demo four']

publisher = pubsub_v1.PublisherClient()

for message in data:
    publisher.publish(topic_name, message)

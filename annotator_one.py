from google.cloud import pubsub_v1

input_subscription_name = 'projects/watchful-net-273116/subscriptions/subscription.one'
output_topic_name = 'projects/watchful-net-273116/topics/topic.two'

subscriber = pubsub_v1.SubscriberClient()
publisher = pubsub_v1.PublisherClient()


def callback(message):
    message_string = str(message.data)
    output_string = message_string.upper()
    publisher.publish(output_topic_name, bytes(output_string, 'utf-8'))
    message.ack()


future = subscriber.subscribe(input_subscription_name, callback)
future.result()

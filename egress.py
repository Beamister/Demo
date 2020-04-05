from google.cloud import pubsub_v1

input_subscription_name = 'projects/watchful-net-273116/subscriptions/subscription.one'

subscriber = pubsub_v1.SubscriberClient()
publisher = pubsub_v1.PublisherClient()


def callback(message):
    message_string = str(message.data)
    print("Received message:", message_string)
    message.ack()


future = subscriber.subscribe(input_subscription_name, callback)
future.result()

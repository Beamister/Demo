from google.cloud import pubsub_v1
import datetime

input_subscription_name = 'projects/Demo/subscriptions/subscription.two'
output_topic_name = 'projects/Demo/topics/topic.three'

subscriber = pubsub_v1.SubscriberClient()
publisher = pubsub_v1.PublisherClient()


def callback(message):
    message_string = str(message.data)
    output_string = message_string + "  --  " + str(datetime.datetime.now())
    publisher.publish(output_topic_name, bytes(output_string))
    message.ack()


future = subscriber.subscribe(input_subscription_name, callback)
future.result()

from google.cloud import pubsub_v1


publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()

topic_one_name = 'projects/Demo/topics/topic.one'
subscription_one_name = 'projects/Demo/subscriptions/subscription.one'

topic_two_name = 'projects/Demo/topics/topic.two'
subscription_two_name = 'projects/Demo/subscriptions/subscription.two'

topic_three_name = 'projects/Demo/topics/topic.three'
subscription_three_name = 'projects/Demo/subscriptions/subscription.three'


publisher.create_topic(topic_one_name)
subscriber.create_subscription(name=subscription_one_name, topic=topic_one_name)

publisher.create_topic(topic_two_name)
subscriber.create_subscription(name=subscription_two_name, topic=topic_two_name)

publisher.create_topic(topic_three_name)
subscriber.create_subscription(name=subscription_three_name, topic=topic_three_name)

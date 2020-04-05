from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()

topic_one_path = 'projects/watchful-net-273116/topics/topic.one'
subscription_one_path = 'projects/watchful-net-273116/subscriptions/subscription.one'

topic_two_path = 'projects/watchful-net-273116/topics/topic.two'
subscription_two_path = 'projects/watchful-net-273116/subscriptions/subscription.two'

topic_three_path = 'projects/watchful-net-273116/topics/topic.three'
subscription_three_path = 'projects/watchful-net-273116/subscriptions/subscription.three'


publisher.create_topic(topic_one_path)
subscriber.create_subscription(name=subscription_one_path, topic=topic_one_path)

publisher.create_topic(topic_two_path)
subscriber.create_subscription(name=subscription_two_path, topic=topic_two_path)

publisher.create_topic(topic_three_path)
subscriber.create_subscription(name=subscription_three_path, topic=topic_three_path)

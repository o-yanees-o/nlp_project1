import tweepy
from keys import bearer_token, consumer_key, consumer_secret, access_token, access_token_secret

iencli = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

response = iencli.create_tweet(text='aaa')

print(response)


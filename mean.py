#Twitter API in Python 
import tweepy

#Authentication information
consumer_key = "85Oi9vtGgOn8cnWlSWyTTK4IT"
consumer_secret = "tzjILX5GSErhjWUGMOloaAB41MiqV7LkvFSVOLVJoglXr5FTCl"
access_token= "1281092401688387584-hHxFksDz8EwSTNQezKLqq0GbRzsCVL"
access_secret = "T5txurL8p5QvkHN7GsqKvGi9Svs0z25eVXOxqfM9Gs0Y4"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

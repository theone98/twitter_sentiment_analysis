import tweepy
from textblob import TextBlob

# NOTE: I put my keys in the keys.py to separate them
# from this main file.
# Please refer to keys_format.py to see the format.
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)


x=input("***ENTER THE SUBJECT OF TWEET***\ninput:")

public_tweets = api.search(x)

for tweet in public_tweets:
    print(tweet.text)
    print('')
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)

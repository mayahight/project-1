"""
    Maya Hightower
    Radical Software, Fall 2021
    Project 1
    Sept 23, 2021
    python3
"""
import tweepy

from authorization_tokens import *

import random

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# here's my tweet template
tweet = "hi my name is ted and i {}"
# here's my options to fill in, mad lib-styles
word_list = ["am canadian",
            "am most definitely NOT the zodiac killer",
            "went to cancun while my state froze over but dw i blamed it on my daughters <3",
            "tried running for president once"]

message = tweet.format(random.choice(word_list))


""" this was my attempt at quote-tweeting, though i had issues with the url situation. """
# # taking tweets from ted's twitter
# ted_tweets = api.user_timeline(screen_name="@tedcruz", exclude_replies=True, include_rts=False)
# # taking ted's tweet
# the_tweet = random.choice(ted_tweets)
#
# print( dir(the_tweet))
#
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(the_tweet._json)
#
# # taking ted's tweet's url
# if "media" in the_tweet.entities:
#     twurl = (the_tweet.entities["media"][0]["expanded_url"])
# else:
#     twurl = (the_tweet.entities["urls"][0]["expanded_url"])
#
# print("here's this: " + twurl)
#
# api.update_status(message, attachment_url=the_tweet.entities["urls"][0]["expanded_url"])

api.update_status(message + " @tedcruz")
print(message)
print("done.")

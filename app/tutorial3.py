
import tweepy

import pronouncing

from authorization_tokens import *

import random

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

message = ""

# #Option5: basic search
#
# search_results = api.search(q="Abbott", lang="en", tweet_mode="extended")
# random_tweet = random.choice(search_results)
#
# # print( dir(random_tweet) )
#
# # import pprint
# # pp = pprint.PrettyPrinter(indent=4)
# # pp.pprint(random_tweet._json)
#
# text = random_tweet.full_text
# message = text.replace("Abbott", "Old Man")
# print(message)

# # Option6: mentions
#
# mentions = api.mentions_timeline()
# mention_tweet = random.choice(mentions)
#
# thanks = " gracias for the mention, u rock"
# message = "@" + mention_tweet.user.screen_name + thanks

# Option7: external API

mentions = api.mentions_timeline()
mention_tweet = random.choice(mentions)
mention_tweet_words = mention_tweet.text.split()

word = random.choice(mention_tweet_words)

rhyming_word_list = pronouncing.rhymes(word)
rhyme_word = random.choice(rhyming_word_list)

print(mention_tweet)
# api.update_status(message)
# api.update_status(message, in_reply_to_status_id=mention_tweet.id)

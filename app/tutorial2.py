import tweepy

from authorization_tokens import *

import random

# # Option1
# tweet_list = [  "ted cruz zodiac killer",
#                 "all my homies hate greg abbott",
#                 "dan patrick sucks"]
#
# tweet_list = [  "pisces superior",
#                 "5 birthdays is a lot of birthdays",
#                 "i didn't have breakfast" ]
#
# message = random.choice(tweet_list)


# # Option2
# tweet_template = "{} is {}"
#
# word1_list = ["pad thai", "ramen noodles", "cereal", "sushi"]
# word2_list = ["scrumdidleeumptious", "delish", "yum", "great"]
#
# word1 = random.choice(word1_list)
# word2 = random.choice(word2_list)
#
# message = tweet_template.format(word1,word2)


# # Option3
# tweet_list = [  "{} is {}",
#                 "{} maintains its {}-ness",
#                 "how could u not like {}, it tastes {}"]
#
# word1_list = ["pad thai", "ramen noodles", "cereal", "sushi"]
# word2_list = ["scrumdidleeumptious", "delish", "yum", "great"]
#
# template = random.choice(tweet_list)
#
# word1 = random.choice(word1_list)
# word2 = random.choice(word2_list)
#
# message = template.format(word1,word2)


# Option4
tweet_template = "{} are {}"

word1_list = ["hot wings", "ramen noodles"]

word2_list_a = ["scrumdidleeumptious", "spicy", "hot"]
word2_list_b = ["slurpy", "fantastic", "to die for"]

word1 = random.choice(word1_list)

if word1 == "hot wings":
    word2 = random.choice(word2_list_a)
elif word1 == "ramen noodles":
    word2 = random.choice(word2_list_b)

message = tweet_template.format(word1,word2)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)
print("Done.")

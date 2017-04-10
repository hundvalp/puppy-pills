#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from backoff_generator import BackoffGenerator
from reminder_message import ReminderMessage
from tweet_builder import TweetBuilder
from random import sample
import tweepy
import config

# Connect to the Twitter API
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.API(auth)

# Create our reminder messages, tweet builder, and backoff timer
reminder_message = ReminderMessage(config.custom_reminders)
tweet_builder = TweetBuilder(config.mention_users)
backoff = BackoffGenerator(5, max_value=3600, exponent=1.55) # Backoff time caps at 1 hour

# Create a randomized list of indices
message_count = reminder_message.get_message_count()
message_indices = sample(range(message_count), message_count - 1)

# Iterate over message indices until one sends successfully
for message_index in message_indices:
    tweet = tweet_builder.create_tweet(reminder_message.get_message(message_index))

    # Attempt sending to twitter
    try:
        api.update_status(tweet)
        break # Sent successfully, stop iterating
    except tweepy.TweepError as e:
        raise e

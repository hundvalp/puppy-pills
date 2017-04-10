# -*- coding: utf-8 -*-

import unittest
from tweet_builder import TweetBuilder

class TestTweetBuilder(unittest.TestCase):
    def test_mention_user_parsing(self):
        verify_parsing = lambda given, expected: self.assertEqual(expected, TweetBuilder(given).create_tweet(''))

        verify_parsing(' twitter', '@twitter ')
        verify_parsing('@twitter', '@twitter ')
        verify_parsing(' twitter  github', '@twitter @github ')
        verify_parsing('@twitter  github', '@twitter @github ')
        verify_parsing(' twitter @github', '@twitter @github ')

        verify_parsing([' twitter'], '@twitter ')
        verify_parsing(['@twitter'], '@twitter ')
        verify_parsing([' twitter', ' github'], '@twitter @github ')
        verify_parsing(['@twitter', ' github'], '@twitter @github ')
        verify_parsing([' twitter', '@github'], '@twitter @github ')
        
    def test_create_tweet(self):
        verify_tweet = lambda given, expected: self.assertEqual(expected, TweetBuilder('twitter').create_tweet(given))

        verify_tweet('Hello world!', '@twitter Hello world!')
        verify_tweet(' Hello world! ', '@twitter  Hello world! ')

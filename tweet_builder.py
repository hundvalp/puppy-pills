# -*- coding: utf-8 -*-

class TweetBuilder(object):
    """Constructs tweets to specific users"""

    def __init__(self, mention_users):
        """Create a new tweet builder which will mention the given users"""
        super(TweetBuilder, self).__init__()

        # Convert lists to a space separated string
        if not isinstance(mention_users, str):
            mention_users = ' '.join(mention_users)

        # Ensure that the mention users string contains an @ before all usernames
        mention_users = ' '.join(mention_users.split()) # Remove multiple consecutive spaces
        mention_users = '@' + mention_users.replace('@', '').replace(' ', ' @')

        # The prefix of each tweet is the users to mention
        self.tweet_prefix = mention_users + ' '

    def create_tweet(self, message):
        """Creates a tweet which mentions the builder's mention users with the given message"""
        return self.tweet_prefix + message

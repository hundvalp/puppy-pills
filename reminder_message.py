# -*- coding: utf-8 -*-

class ReminderMessage(object):
    """Provides a list of reminder messages which can be accessed individually"""

    default_reminder_messages = (
        "It's time for your pills!",
        "Don't forget your pills, sweetie!",
        "Did you remember your meds today?~",
        "💊🐾",
        "Hoping it's a good day for you, don't forget your meds ❤️",
        "Don't forget to drink plenty of water and take your pills ❤️",
        "If you're feeling down, remember to take your meds and try some exercises!",
        "I love you, please remember your meds today ❤️",
        "Don't forget to drink plenty of water with your medicine today ❤️",
        "It's easy to forget your medication, that's why I'm here to help you! ❤️",
    )

    def __init__(self, custom_reminder_messages=()):
        """Creates a new puppy pills reminder object with an optional list of custom reminder messages"""
        super(ReminderMessage, self).__init__()
        self.reminder_messages = ReminderMessage.default_reminder_messages + tuple(custom_reminder_messages)
        self.reminder_messages_length = len(self.reminder_messages)

    def get_message_count(self):
        """Returns the number of reminder messages this object contains"""
        return self.reminder_messages_length

    def get_message(self, index):
        """Returns the message at the given index. Index is capped within range"""
        if index < 0:
            index = 0
        elif index >= self.reminder_messages_length:
            index = self.reminder_messages_length - 1

        return self.reminder_messages[index]

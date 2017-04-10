# -*- coding: utf-8 -*-

import unittest
from reminder_message import ReminderMessage

class TestReminderMessage(unittest.TestCase):
    def test_message_count(self):
        """Verify that the correct message count is returned"""
        default_length = len(ReminderMessage.default_reminder_messages)

        testObject = ReminderMessage()
        self.assertEqual(default_length + 0, testObject.get_message_count())

        testObject = ReminderMessage(['abc'])
        self.assertEqual(default_length + 1, testObject.get_message_count())

        testObject = ReminderMessage(['abc', 'def', 'ghi'])
        self.assertEqual(default_length + 3, testObject.get_message_count())

    def test_get_message(self):
        default_length = len(ReminderMessage.default_reminder_messages)

        testObject = ReminderMessage(['abc', 'def'])
        self.assertEqual("It's time for your pills!", testObject.get_message(0))
        self.assertEqual('abc', testObject.get_message(default_length + 0))
        self.assertEqual('def', testObject.get_message(default_length + 1))

        # Ensure that the index is capped
        self.assertEqual("It's time for your pills!", testObject.get_message(-100))
        self.assertEqual('def', testObject.get_message(100))

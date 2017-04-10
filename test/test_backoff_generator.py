# -*- coding: utf-8 -*-

import unittest
from backoff_generator import BackoffGenerator

class TestBackoffGenerator(unittest.TestCase):
    def test_next_value(self):
        backoff = BackoffGenerator(2, exponent=2)

        verify_backoff = lambda expected: self.assertEqual(expected, backoff.next())

        verify_backoff(2)
        verify_backoff(4)
        verify_backoff(16)
        verify_backoff(256)
        verify_backoff(65536)

    def test_next_value_with_max(self):
        backoff = BackoffGenerator(2, max_value=50, exponent=2)

        verify_backoff = lambda expected: self.assertEqual(expected, backoff.next())

        verify_backoff(2)
        verify_backoff(4)
        verify_backoff(16)
        verify_backoff(50)
        verify_backoff(50)

    def test_reset(self):
        backoff = BackoffGenerator(2, max_value=50, exponent=2)

        verify_backoff = lambda expected: self.assertEqual(expected, backoff.next())

        verify_backoff(2)
        verify_backoff(4)
        verify_backoff(16)
        verify_backoff(50)
        verify_backoff(50)

        backoff.reset()

        verify_backoff(2)
        verify_backoff(4)
        verify_backoff(16)
        verify_backoff(50)
        verify_backoff(50)

# -*- coding: utf-8 -*-

class BackoffGenerator(object):
    """Generates a sequence of values for use in backoff timing"""

    def __init__(self, initial_value, max_value=None, exponent=2):
        """Sets the initial value, max value, and exponent for the backoff"""
        super(BackoffGenerator, self).__init__()
        self.value = initial_value
        self.initial_value = initial_value
        self.max_value = max_value
        self.exponent = exponent
        
    def next(self):
        """Returns the next value for the backoff"""
        next_value = self.value

        # Update the value for the next call
        if self.max_value is None or self.value != self.max_value:
            self.value **= self.exponent

            if not self.max_value is None and self.value > self.max_value:
                self.value = self.max_value

        return next_value

    def reset(self):
        self.value = self.initial_value

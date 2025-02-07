#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            print("The value must be a string.")
            self._value = ""
        else:
            self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        """Check if the value ends with a period."""
        return self._value.endswith(".")

    def is_question(self):
        """Check if the value ends with a question mark."""
        return self._value.endswith("?")

    def is_exclamation(self):
        """Check if the value ends with an exclamation mark."""
        return self._value.endswith("!")

    def count_sentences(self):
        """
        Returns the number of sentences in the value.
        A sentence is defined as ending with '.', '!', or '?'.
        """
        import re
        sentences = re.split(r"[.!?]+", self._value.strip())
        return len([s for s in sentences if s.strip()])  # Filter out empty strings

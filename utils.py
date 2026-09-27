def is_palindrome(s):
    """Check whether a string is a palindrome."""
    return s == s[::-1]


def count_words(text):
    """Count the number of words in a text."""
    return len(text.split())


def celsius_to_fahrenheit(c):
    """Convert Celsius temperature to Fahrenheit."""
    return (c * 9 / 5) + 32
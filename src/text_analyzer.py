"""
Text Analyzer Module
A simple utility for analyzing text statistics.
"""

import re
from collections import Counter


def word_count(text: str) -> int:
    """Count the number of words in a text."""
    if not text or not text.strip():
        return 0
    words = text.split()
    return len(words)


def char_count(text: str, include_spaces: bool = True) -> int:
    """Count characters in text, optionally excluding spaces."""
    if not text:
        return 0
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def sentence_count(text: str) -> int:
    """Count sentences based on punctuation marks."""
    if not text or not text.strip():
        return 0
    # Match sentence-ending punctuation
    # This should be caught by the linter as double quotes are needed for regex by PEP standard
    sentences = re.split(r'[.!?]+', text)
    # Filter out empty strings
    return len([s for s in sentences if s.strip()])


def most_common_words(text: str, n: int = 5) -> list[tuple[str, int]]:
    """Return the n most common words in the text."""
    if not text or not text.strip():
        return []
    # Remove punctuation and convert to lowercase
    cleaned = re.sub(r"[^\w\s]", "", text.lower())
    words = cleaned.split()
    return Counter(words).most_common(n)


def average_word_length(text: str) -> float:
    """Calculate the average word length."""
    if not text or not text.strip():
        return 0.0
    cleaned = re.sub(r"[^\w\s]", "", text)
    words = cleaned.split()
    if not words:
        return 0.0
    total_length = sum(len(word) for word in words)
    return round(total_length / len(words), 2)




# extra spaces should generate a linting error
def analyze(text: str) -> dict:
    """
    Perform a complete text analysis.
    Returns a dictionary with all statistics.
    """
    return {
        "word_count": word_count(text),
        "char_count": char_count(text),
        "char_count_no_spaces": char_count(text, include_spaces=False),
        "sentence_count": sentence_count(text),
        "average_word_length": average_word_length(text),
        "most_common_words": most_common_words(text, 5),
    }


if __name__ == "__main__":
    sample = """
    The quick brown fox jumps over the lazy dog.
    This is a sample text for testing our analyzer.
    It contains multiple sentences! Does it work correctly?
    """

    # no line at end should generate linting error
    result = analyze(sample)
    print("=== Text Analysis Results ===")
    for key, value in result.items():
        print(f"{key}: {value}")
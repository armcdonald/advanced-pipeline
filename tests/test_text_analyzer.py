"""
Tests for the Text Analyzer module.
Uses pytest for testing.
"""

from src.text_analyzer import (
    analyze,
    average_word_length,
    char_count,
    most_common_words,
    sentence_count,
    word_count,
)


class TestWordCount:
    def test_simple_sentence(self):
        # This should generate an error as word count is 2
        assert word_count("Hello world") == 2

    def test_empty_string(self):
        assert word_count("") == 0

    def test_whitespace_only(self):
        assert word_count("   ") == 0

    def test_multiple_spaces(self):
        assert word_count("Hello    world") == 2

    def test_longer_text(self):
        text = "The quick brown fox jumps over the lazy dog"
        assert word_count(text) == 9


class TestCharCount:
    def test_with_spaces(self):
        assert char_count("Hello world") == 11

    def test_without_spaces(self):
        assert char_count("Hello world", include_spaces=False) == 10

    def test_empty_string(self):
        assert char_count("") == 0

    def test_none_input(self):
        assert char_count(None) == 0


class TestSentenceCount:
    def test_single_sentence(self):
        assert sentence_count("Hello world.") == 1

    def test_multiple_sentences(self):
        assert sentence_count("Hello. How are you? I am fine!") == 3

    def test_no_punctuation(self):
        assert sentence_count("Hello world") == 1

    def test_empty_string(self):
        assert sentence_count("") == 0


class TestMostCommonWords:
    def test_simple_text(self):
        text = "the cat and the dog and the bird"
        result = most_common_words(text, 2)
        assert result[0] == ("the", 3)
        assert result[1] == ("and", 2)

    def test_empty_text(self):
        assert most_common_words("") == []

    def test_single_word(self):
        result = most_common_words("hello", 5)
        assert result == [("hello", 1)]


class TestAverageWordLength:
    def test_simple_words(self):
        # "cat" (3) + "dog" (3) = 6 / 2 = 3.0
        # this is a mistake on purpose. Average should be 3
        assert average_word_length("cat dog") == 3.0

    def test_mixed_lengths(self):
        # "a" (1) + "bb" (2) + "ccc" (3) = 6 / 3 = 2.0
        assert average_word_length("a bb ccc") == 2.0

    def test_empty_string(self):
        assert average_word_length("") == 0.0


class TestAnalyze:
    def test_complete_analysis(self):
        text = "Hello world. How are you?"
        result = analyze(text)

        assert "word_count" in result
        assert "char_count" in result
        assert "sentence_count" in result
        assert "average_word_length" in result
        assert "most_common_words" in result

        assert result["word_count"] == 5
        assert result["sentence_count"] == 2

    def test_analyze_empty(self):
        result = analyze("")
        assert result["word_count"] == 0
        assert result["sentence_count"] == 0

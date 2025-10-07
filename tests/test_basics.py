from src.basics import is_even, sum_list, count_words

def test_is_even():
    assert is_even(0) is True
    assert is_even(2) is True
    assert is_even(7) is False
    assert is_even(-4) is True

def test_sum_list_small():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([]) == 0
    assert sum_list([10, -5, 2]) == 7

def test_count_words_basic():
    assert count_words("hello world") == 2
    assert count_words("  spaced   out  ") == 2
    assert count_words("") == 0
    assert count_words("one") == 1

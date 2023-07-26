import pytest
from lib.single_function_ex_1 import *


"""
words_per_minute = 200

text 

reading_time = text/words_per_minute


"""

# 

def test_for_200():
    result = text_passage("string "*200)
    assert result == 1.0
    
def test_for_400():
    result = text_passage("string "*400)
    assert result == 2.0


def test_for_300():
    result = text_passage("string "*300)
    assert result == 1.5


def test_for_empty_string():
    with pytest.raises(Exception) as e:
        text_passage("")
    error_message = str(e.value)
    assert error_message == "Text is empty"
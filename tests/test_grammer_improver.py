import pytest
from lib.grammar_improver import *


"""
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

function name - grammar_improver()
argument - take string input called "text"
return with a message stating if the capital letters are in the right place and puntuation is in the right place


test_text_with_no_grammar_mistakes
first test - one short sentence like "Hi, my name is.." which will be the argument
return "correct use of grammar"

test_text_with_no_punctuation
second test - 
argument - "Hi my name is bob"
return "incorrect use of grammar"

test_text_with_no_capitalised_letter
third test - 
argument - "hi my name is bob."
return "incorrect use of grammar"

test_text_with_no_punctuation_or_capitalised_letter
fourth test - 
argument - "hi my name is bob"
return "incorrect use of grammar"

test_text_with_empty_string
fifth test 
argument - ""
return - error message - "No text input provided"
"""


def test_text_with_no_grammar_mistakes():
    result = grammar_improver("Hi, my name is Bob." )
    assert result == "Correct use of grammar"

def test_text_with_no_punctuation():
    result = grammar_improver("Hi my name is bob")
    assert result == "Incorrect use of grammar"

def test_text_with_no_capitalised_letter():
    result = grammar_improver("hi my name is bob.")
    assert result == "Incorrect use of grammar"
    
def test_text_with_no_punctuation_or_capitalised_letter():
    result = grammar_improver("hi my name is bob")
    assert result == "Incorrect use of grammar"


def test_text_with_no_punctuation_or_capitalised_letter():
    with pytest.raises(Exception) as e:
       grammar_improver("")
    error_message = str(e.value)
    assert error_message == "No text input provided"

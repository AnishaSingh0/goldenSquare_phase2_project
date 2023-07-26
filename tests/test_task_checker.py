import pytest
from lib.task_checker import *

"""
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

function name - is_task()
argument - text as string 
returning boolean True or False 

test 1 - test_text_only_includes_TODO
argument - "#TODO"
returns - True 

test 2 - test_text_includes_no_TODO
argument - "Once upon on a time"
returns - False

test 3 - test_text_includes_TODO_in_middle
argument - "washing my clothes is my #TODO for tomorrow"
return - True 

test 4 - test_text_string_is_empty
argument - ""
return - Exception - "No text input"

test 5 - test_text_includes_only_TODO_without_hash
argument - "TODO for tomorrow"
return - False

-- assuming that lower case todo does not count --
test 6 - test_text_includes_lowercase_todo
argument - "#todo for tomorrow"
return - False 

test 7 - test_text_includes_ToDo_with_alternating_CAPs
argument - "Tomorrow's #ToDo"
return - False
"""

#test 1 

def test_text_only_includes_TODO():
    result = is_task("#TODO")
    assert result == True 
    
#test 2 

def test_text_includes_no_TODO():
    result = is_task("Once upon on a time")
    assert result == False
    
#test 3 

def test_text_includes_TODO_in_middle():
    result = is_task("washing my clothes is my #TODO for tomorrow")
    assert result == True

#test 4

def test_text_string_is_empty():
    with pytest.raises(Exception) as e:
        is_task("")
    error_message = str(e.value)
    assert error_message == "No text input"

# test 5 

def test_text_includes_only_TODO_without_hash():
    result = is_task("washing my clothes is my TODO for tomorrow")
    assert result == False

# test 6 

def test_text_includes_lowercase_todo():
    result = is_task("washing my clothes is my #todo for tomorrow")
    assert result == False

#test 7
def test_text_includes_ToDo_with_alternating_CAPs():
    result = is_task("washing my clothes is my #ToDo for tomorrow")
    assert result == False
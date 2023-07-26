import pytest
from lib.personal_diary import *

def test_personal_diary_first_five_chars():
    snippet = make_snippet("Yesterday I went")
    assert snippet[0:5] + "..." == "Yeste..."



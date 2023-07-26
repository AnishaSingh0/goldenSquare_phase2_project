import pytest
from lib.countWords import *


def test_countWords_valid():
    result = countWords("Today is a good day")
    assert result == 5



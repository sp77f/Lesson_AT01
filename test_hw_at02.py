import pytest
from hw_at02 import count

def test_count():
    assert count("привет") == 2

@pytest.mark.parametrize("word,exp", [
    ('аиеу', 4),
    ('ПРИВЕТ о мой МИР', 5)
    ])
def test_check3(word, exp):
    assert count(word) == exp
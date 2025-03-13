import pycodestyle

from regex import find_uuu

def test_pep8():
    style_checker = pycodestyle.StyleGuide(quiet=False)
    result = style_checker.check_files(['pep8.py'])
    assert result.total_errors == 0

def test_find_uuu():
    assert find_uuu("Ubuntu")
    assert find_uuu("ubuntu")
    assert find_uuu("uuu")
    assert find_uuu("uUu")
    assert find_uuu("GugugajUu")
    assert not find_uuu("uu")
    assert not find_uuu("")
    assert not find_uuu("Underworld")
    assert not find_uuu("Ululate")

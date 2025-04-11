from lib.design_and_test_drive import *

def test_if_empty_string():
    assert includes_todo("") == False

def test_if_todo_is_there():
    assert includes_todo("#TODO Walk the dog") == True

def test_todo_without_hash():
    assert includes_todo("TODO Walk the dog") == False

def test_if_no_todo():
    assert includes_todo("Walk the dog") == False

def test_if_todo_lower():
    assert includes_todo("#todo Walk the dog") == False

def test_if_todo_in_word():
    assert includes_todo("Walk th#TODOe dog") == True
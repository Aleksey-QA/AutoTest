import pytest
def test_user(user):
    print("+++Запустили тест+++")
    assert  user.get('name') == "Alica"
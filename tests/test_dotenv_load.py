import os


def test_load():
    assert os.environ.get("MY_AUTODOTENV_VARIABLE") == "MY_VALUE"
    assert os.environ.get("MY_AUTODOTENV_VARIABLE_DEL") is None

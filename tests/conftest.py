import pytest


@pytest.fixture(autouse=True)
def clean_file():
    with open('text.txt', "w"):
        pass
from Functions.file_read import read_from_file
import pytest


def create_test_data(test_data):
    with open('text.txt', 'a') as file:
        file.writelines(test_data)


def test_read_from_file():
    test_data = ['First line\n', 'Second line\n', 'Third line\n']
    create_test_data(test_data)
    assert test_data == read_from_file('text.txt')

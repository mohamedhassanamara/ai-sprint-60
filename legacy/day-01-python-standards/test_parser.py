from pydantic import ValidationError

from parser import clean_json_data
import pytest
import json

@pytest.fixture
def valid_data(tmp_path):
    # create a file that has valid data
    filepath = tmp_path / 'valid_data.json'
    dummy_data = [
        {"name": "John", "age": 30, "email": "john.doe@email.com"},
        {"name": "Jane", "age": 25, "email": "jane.doe@email.com"}
    ]
    with open(filepath, 'w') as f:
        json.dump(dummy_data, f)

    yield str(filepath)
    # remove the file after the test
    import os
    os.remove(filepath)

@pytest.fixture
def invalid_data(tmp_path):
    filepath = tmp_path / 'invalid_data.json'
    dummy_data = [
        {"name": "John12", "age": 30, "email": "john.doe@emailcom"},
        {"name": "Jane", "age": 25, "email": "jane.doe@email.com"},
        {"name": "Bob", "age": "thirty", "email": ""}
    ]
    with open(filepath, 'w') as f:
        json.dump(dummy_data, f)
    yield str(filepath)
    # remove the file after the test
    import os
    os.remove(filepath)


def test_clean_json_data_valid(valid_data):
    users = clean_json_data(valid_data)
    assert len(users) == 2
    assert users[0].name == "John"
    assert users[0].age == 30
    assert users[0].email == "john.doe@email.com"

def test_clean_json_data_invalid(invalid_data):
    with pytest.raises(ValidationError):
        clean_json_data(invalid_data)
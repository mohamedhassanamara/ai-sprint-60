from pydantic import ValidationError

from models import User
import json

def clean_json_data(filepath: str) -> list[User]:
    user_list = []
    # open file from filepath
    with open(filepath, 'r') as f:
        data = json.load(f)
        for record in data:
            try:
                user = User(**record)
                user_list.append(user)
            except ValidationError as e:
                print(f"Error parsing record: {record}. Error: {e}")
                raise
        return user_list

if __name__ == "__main__":
    users = clean_json_data('raw_data.json')
    print(users)
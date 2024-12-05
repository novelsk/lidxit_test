import json
from pprint import pprint

from app.db import db

if __name__ == '__main__':
    collection = db["templates"]
    collection.delete_many({})
    with open('fixture.json') as f:
        data = json.load(f)
    result = collection.insert_many(data)
    pprint(data)
    print(f"Вставлено {len(result.inserted_ids)} форм.")

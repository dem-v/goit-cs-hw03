from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

MONGO_CONSTR = "mongodb://admin:password@localhost:27017/test?retryWrites=true&w=majority&authSource=admin"

client = MongoClient(
    MONGO_CONSTR,
    server_api=ServerApi('1')
)


# Приймає один json документ, повертає ObjectId
def insert_one(json: dict) -> ObjectId | None:
    try:
        db = client.test
    except Exception as e:
        print(e)
        return None

    try:
        return db.cats.insert_one(json).inserted_id
    except Exception as e:
        print(e)
        return None


# Приймає один чи декілька json документів у списку, повертає список ObjectId
def insert_many(json: list[dict]) -> list[ObjectId] | None:
    try:
        db = client.test
    except Exception as e:
        print(e)
        return None

    try:
        return db.cats.insert_many(json).inserted_ids
    except Exception as e:
        print(e)
        return None


# Приймає словник фільтрів або пустий, повертає dict
def find_one(json: dict = {}) -> dict | None:
    try:
        db = client.test
    except Exception as e:
        print(e)
        return None

    try:
        return db.cats.find_one(json)
    except Exception as e:
        print(e)
        return None


# Приймає словник фільтрів або пустий, повертає список знайдених об'єктів
def find_many(json: dict = {}) -> list[dict] | None:
    try:
        db = client.test
    except Exception as e:
        print(e)
        return None

    try:
        return [i for i in db.cats.find(json)]
    except Exception as e:
        print(e)
        return None


# Приймає словник фільтрів та словник змін, повертає число оновлених об'єктів - оновлює тільки перший об'єкт
def update_one(json: dict, upd: dict) -> int | None:
    try:
        db = client.test
    except Exception as e:
        print(e)
        return None

    try:
        return db.cats.update_one(json, upd).modified_count
    except Exception as e:
        print(e)
        return None


# Приймає словник фільтрів та словник змін, повертає число оновлених об'єктів
def update_many(json: dict, upd: dict) -> int | None:
    try:
        db = client.test
    except Exception as e:
        print(e)
        return None

    try:
        return db.cats.update_many(json, upd).modified_count
    except Exception as e:
        print(e)
        return None


# Приймає словник фільтрів, повертає число видалених об'єктів - видаляє тільки перший
def delete_one(json: dict) -> int | None:
    try:
        db = client.test
    except Exception as e:
        print(e)
        return None

    try:
        return db.cats.delete_one(json).deleted_count
    except Exception as e:
        print(e)
        return None


# Приймає словник фільтрів, повертає число видалених об'єктів
def delete_many(json: dict = {}) -> int | None:
    try:
        db = client.test
    except Exception as e:
        print(e)
        return None

    try:
        return db.cats.delete_many(json).deleted_count
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    result_one = insert_one(
        {
            "name": "barsik",
            "age": 3,
            "features": ["ходить в капці", "дає себе гладити", "рудий"],
        }
    )
    print(result_one)

    result_many = insert_many(
        [
            {
                "name": "Lama",
                "age": 2,
                "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
            },
            {
                "name": "Liza",
                "age": 4,
                "features": ["ходить в лоток", "дає себе гладити", "білий"],
            },
        ]
    )
    print(result_many)

    print(find_one({"name": "Lama"}))
    print(find_many({"age": 4}))
    print(find_many())
    print(find_one({"_id": ObjectId("60d24b783733b1ae668d4a77")}))

    print(update_one({"name": "barsik"}, {"$set": {"age": 4}}))
    print(find_one({"name": "barsik"}))

    print(delete_one({"name": "barsik"}))
    print(find_one({"name": "barsik"}))

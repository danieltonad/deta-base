import uuid

def test_serializer(user) -> dict:
    return {
        "id": str(user['_id']),
        "email": user['email']
    }


def tests_serializer(users) -> list:
    return [test_serializer(user) for user in users]
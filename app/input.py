from app.config import get_database
from app.models import User

def insert_random_users():
    db = get_database()
    users_collection = db["users"]
    for _ in range(100):
        user = User.generate_random_user()
        users_collection.insert_one(user.dict())


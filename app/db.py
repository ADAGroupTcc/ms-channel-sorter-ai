from app.config import get_database

db = get_database()
users_collection = db["users"]
categories_collection = db["categories"]
channels_collection = db['channels']
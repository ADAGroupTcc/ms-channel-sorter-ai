from pymongo import MongoClient
from dotenv import load_dotenv
import os

def get_database():
    load_dotenv()
    client = MongoClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017/"))
    db = client[os.getenv("MONGODB_DBNAME", "localdb")]
    return db

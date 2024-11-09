from bson import ObjectId
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import random
from app.db import categories_collection
from faker import Faker

class Categoria(BaseModel):
    id: str
    name: str

class User(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    description: Optional[str]
    nickname: Optional[str]
    cpf: str
    location: List[float]
    categories: List[object]
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def generate_random_user():
        fake = Faker()
        categories = categories_collection.find({})
        categoriesIds = [ObjectId(category["_id"]) for category in categories]
        return User(
            id="",
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            description=fake.sentence(nb_words=4) if random.choice([True, True]) else None,
            nickname=fake.user_name() if random.choice([True, True]) else None,
            cpf=fake.ssn(),
            location=[fake.latitude(), fake.longitude()],
            categories=categoriesIds,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

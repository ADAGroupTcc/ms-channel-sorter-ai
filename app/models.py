from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId
from datetime import datetime
from faker import Faker
import random

fake = Faker()

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
        return User(
            id=str(ObjectId()),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            description=fake.text(max_nb_chars=200),
            nickname=fake.user_name(),
            cpf=fake.ssn(),
            location=[fake.latitude(), fake.longitude()],
            categories=random.sample([
            ObjectId("6729462956fb7da155915495"),
            ObjectId("6729463256fb7da155915d9a"),
            ObjectId("6729463c56fb7da15591684a"),
            ObjectId("6729464356fb7da1559170a8"),
            ObjectId("6729464956fb7da1559177a6"),
            ObjectId("6729465156fb7da155917ee4"),
            ObjectId("6729465756fb7da1559184df"),
            ObjectId("6729465c56fb7da155918a65"),
            ObjectId("6729466256fb7da155919012"),
            ObjectId("6729466756fb7da1559194e4"),
            ObjectId("6729466f56fb7da155919cfd"),
            ObjectId("6729467556fb7da15591a32b")
            ], random.randint(4, 12)),
            created_at=fake.date_time_this_decade(),
            updated_at=fake.date_time_this_decade()
        )

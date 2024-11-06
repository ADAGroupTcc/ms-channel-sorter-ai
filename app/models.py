from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import random

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

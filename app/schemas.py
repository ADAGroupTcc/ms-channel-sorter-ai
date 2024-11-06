from pydantic import BaseModel
from typing import List

class UserSchema(BaseModel):
    id: str
    first_name: str
    last_name: str
    location: List[float]
    interests: List[str]

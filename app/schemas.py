from pydantic import BaseModel

class UserSchema(BaseModel):
    id: str
    first_name: str
    last_name: str
    nickname: str

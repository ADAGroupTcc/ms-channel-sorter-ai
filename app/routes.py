from fastapi import APIRouter, HTTPException
from app.db import users_collection, categories_collection
from app.models import User, Categoria
from app.schemas import UserSchema
from app.clustering import cluster_users
from bson import ObjectId

router = APIRouter()

@router.get("/v1/search", response_model=dict)
async def search(user_id: str):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    all_users = list(users_collection.aggregate([{
        "$lookup": {
            "from": "categories",
            "localField": "categories",
            "foreignField": "_id",
            "as": "categories"
        }
    }]))
    
    users = []
    for u in all_users:
        user_obj = User(
            id=str(u["_id"]),
            first_name=u["first_name"],
            last_name=u["last_name"],
            email=u["email"],
            description=u.get("description"),
            nickname=u.get("nickname"),
            cpf=u["cpf"],
            location=u["location"],
            categories=[cat["name"] for cat in u["categories"]],
            created_at=u["created_at"],
            updated_at=u["updated_at"]
        )
        users.append(user_obj)
    
    clustered_users = cluster_users(users, user_id)
    
    common_categories = set(clustered_users[0].categories)
    for user in clustered_users[1:]:
        common_categories.intersection_update(user.categories)
    
    return {
        "users": [
            UserSchema(
                id=user.id,
                first_name=user.first_name,
                last_name=user.last_name,
                nickname=user.nickname,
            ) for user in clustered_users
        ],
        "categories": list(common_categories)
    }

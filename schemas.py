from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

class UserListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[User]

from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    username: str = Field(
        alias="name",
        title="The username",
        description="This is the user name",
        min_length=1,
        max_length=20,
        default=None
    )
    liked_posts: list[int] = Field(
        description="Array of posts users",
        min_items=2,
        max_items=10
    )


class FullUserProfile(User):
    short_description: str
    long_bio: str


class MultipleUsersResponse(BaseModel):
    users: list[FullUserProfile]
    total: int


class CreateUserResponse(BaseModel):
    user_id: int

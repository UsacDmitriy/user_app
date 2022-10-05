from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


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


profile_infos = {
    0:
        {
            "short_description": "My bio description",
            "long_bio": "This is our long bio",
        },
}
user_contents = {
    0:
        {
            "name": "Malik",
            "liked_posts": [1, 2],
         },
}


async def get_user_info(user_id: int = 0) -> FullUserProfile:
    # username = 'test user'
    # short_description = 'my bio description'
    # liked_posts = []

    profile_info = profile_infos[user_id]
    user_content = user_contents[user_id]
    user = User(**user_content)

    full_user_profile = {
        **profile_info,
        **user.dict(),
    }

    return FullUserProfile(**full_user_profile)


async def get_all_users_with_pagination(start, limit) -> (list[FullUserProfile], int):
    list_of_users = []
    keys = list(profile_infos.keys())
    total = len(keys)
    for index in range(0, len(keys), 1):
        if index < start:
            continue
        current_key = keys[index]
        user = await get_user_info(current_key)
        list_of_users.append(user)
        if len(list_of_users) >= limit:
            break

    return list_of_users, total


async def create_update_user(full_profile_info: FullUserProfile, new_user_id: Optional[int] = None) -> int:
    """
    Create or update user

    :param full_profile_info:
    :param new_user_id:
    :return:
    """
    global profile_infos
    global user_contents

    if new_user_id is None:
        new_user_id = len(profile_infos)
    liked_posts = full_profile_info.liked_posts
    short_description = full_profile_info.short_description
    long_bio = full_profile_info.long_bio

    user_contents[new_user_id] = {"liked_posts": liked_posts}
    profile_infos[new_user_id] = {
        "short_description": short_description,
        "long_bio": long_bio
    }
    return new_user_id


async def delete_user(user_id: int) -> None:
    global profile_infos
    global user_contents

    del profile_infos[user_id]
    del user_contents[user_id]


@app.get('/user/me', response_model=FullUserProfile)
async def test_endpoint():
    full_user_profile = await get_user_info()
    return full_user_profile


@app.get('/user/{user_id}', response_model=FullUserProfile)
async def get_user_by_id(user_id: int):
    """

    :param user_id:
    :return:
    """

    full_user_profile = await get_user_info(user_id)
    return full_user_profile




@app.put("/user/{user_id}")
async def update_user(user_id: int, full_profile_name: FullUserProfile):
    await create_update_user(full_profile_name, user_id)
    return None


@app.delete("/user/{user_id}")
async def delete_user_by_id(user_id: int):
    await delete_user(user_id)


@app.get("/users", response_model=MultipleUsersResponse)
async def get_all_users_paginated(start: int = 0, limit: int = 2):
    users, total = await get_all_users_with_pagination(start, limit)
    formatted_users = MultipleUsersResponse(users=users, total=total)
    return formatted_users


@app.post("/users", response_model=CreateUserResponse)
async def add_user(full_profile_name: FullUserProfile):
    user_id = await create_update_user(full_profile_name)
    created_user = CreateUserResponse(user_id=user_id)
    return created_user

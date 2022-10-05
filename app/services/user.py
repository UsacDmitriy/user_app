from app.schemas.user import FullUserProfile, User
from typing import Optional

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


class UserService:

    def __init__(self):
        pass

    async def get_all_users_with_pagination(self, start, limit) -> (list[FullUserProfile], int):
        list_of_users = []
        keys = list(profile_infos.keys())
        total = len(keys)
        for index in range(0, len(keys), 1):
            if index < start:
                continue
            current_key = keys[index]
            user = await self.get_user_info(current_key)
            list_of_users.append(user)
            if len(list_of_users) >= limit:
                break

        return list_of_users, total

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    async def delete_user(user_id: int) -> None:
        global profile_infos
        global user_contents

        del profile_infos[user_id]
        del user_contents[user_id]

from fastapi import APIRouter, HTTPException
from app.schemas.user import FullUserProfile, MultipleUsersResponse, CreateUserResponse
from app.services.user import UserService
import logging

logger = logging.getLogger(__name__)
# logging.basicConfig(
#     format='%(levelname)-6s %(name)-15s %(asctime)s %(message)s',
#     datefmt="%y-%m-%d %H-%M-%S",
#     filename='log.txt',
#
# )
logger.setLevel(logging.INFO)  # debug -> infor -> warning -> error -> critical

console = logging.StreamHandler()
# full_logger =  logging.getLogger('')
logger.addHandler(console)


def create_user_router() -> APIRouter:
    user_router = APIRouter(prefix='/user', tags=['user'])
    user_service = UserService()

    @user_router.get("/all", response_model=MultipleUsersResponse)
    async def get_all_users_paginated(start: int = 0, limit: int = 2):
        users, total = await user_service.get_all_users_with_pagination(start, limit)
        formatted_users = MultipleUsersResponse(users=users, total=total)
        return formatted_users

    # @user_router.get('/user/me', response_model=FullUserProfile)
    # async def test_endpoint():
    #     full_user_profile = await user_service.get_user_info()
    #     return full_user_profile

    @user_router.get('/{user_id}', response_model=FullUserProfile)
    async def get_user_by_id(user_id: int):

        # try:
        full_user_profile = await user_service.get_user_info(user_id)
        # except KeyError:
        #     logger.error(f"Non-existed user {user_id} was requested")
        #     raise HTTPException(status_code=404, detail="User does not exist")
        return full_user_profile

    @user_router.put("/{user_id}")
    async def update_user(user_id: int, full_profile_name: FullUserProfile):
        await user_service.create_update_user(full_profile_name, user_id)
        return None

    @user_router.delete("/{user_id}")
    async def delete_user_by_id(user_id: int):
        # logger.debug('This is debug log')
        # logger.info(f"About to delete user {user_id}")
        # try:
        await user_service.delete_user(user_id)
        # except KeyError:
        #     logger.error(f"Non-existed user {user_id} was requested")
        #     raise HTTPException(status_code=404, detail=f"User{user_id} did not exist")

    @user_router.post("/", response_model=CreateUserResponse)
    async def add_user(full_profile_name: FullUserProfile):
        user_id = await user_service.create_update_user(full_profile_name)
        created_user = CreateUserResponse(user_id=user_id)
        return created_user

    return user_router

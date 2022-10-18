import pytest
from app.services.user import UserService
from app.exceptions import UserNoTFound


@pytest.mark.asyncio
async def test_delete_user_properly(user_service, valid_user_id):
    user_to_delete = 0
    await user_service.delete_user(valid_user_id)
    assert valid_user_id not in user_service.profile_infos
    assert valid_user_id not in user_service.user_contents

@pytest.mark.asyncio
async def test_delete_invalid_user_raises_proper_exception(user_service, invalid_user_id):
    with pytest.raises(UserNoTFound):
        await user_service.delete_user(invalid_user_id)
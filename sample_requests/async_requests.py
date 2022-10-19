import aiohttp
import asyncio


async def sample_async_get_request(base_url: str, endpoint_prefix: str, user_id: int) -> (int, dict):
    url = base_url + endpoint_prefix + str(user_id)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            json_response = await response.json()
            status_code = response.status

            return status_code, json_response


async def sample_async_post_request():
    sample_data = {
        "name": "bob",
        "liked_posts": [
            0,
            0,
            1,
            2,
        ],
        "short_description": "string",
        "long_bio": "string"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post('http://127.0.0.1:8000/user/', json=sample_data) as response:
            print(response.status)
            print(response.headers)
            print(await response.json())


# asyncio.run(sample_async_post_request())

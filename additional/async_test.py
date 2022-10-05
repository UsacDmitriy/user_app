import asyncio


async def sleep_a_little(time_to_sleep):
    await asyncio.sleep(time_to_sleep)


async def go_to_do_something():
    time_to_sleep= 10
    await sleep_a_little(time_to_sleep)


asyncio.run(go_to_do_something())
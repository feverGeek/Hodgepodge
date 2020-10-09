import asyncio
import aiohttp


async def post(url, headers, params, semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=params, headers=headers) as response:
                return await response.read()


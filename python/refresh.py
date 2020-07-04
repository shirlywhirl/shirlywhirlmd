import aiohttp
import asyncio
import fire


async def _get(session, url):
    async with session.get(url) as resp:
        return await resp.text()


async def python():
    async with aiohttp.ClientSession() as session:
        html = await _get(session, "http://python.org")
        print(html)


def hello():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(python())


if __name__ == "__main__":
    fire.Fire()

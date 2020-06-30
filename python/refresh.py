import aiohttp
import asyncio
import fire
import json
import os


async def _get(session, url, token):
    params = {grant_type: "ig_refresh_token", access_token: token}
    async with session.get(url, params) as resp:
        assert resp.ok, resp.message
        return await resp.text()


async def _refresh_token(path):
    data = None
    with open(path) as f:
        data = f.read()
    assert data, "No data found at path"

    with aiohttp.ClientSession() as session:
        html = await _get(
            session, "https://graph.instagram.com/refresh_access_token", data
        )
        print(html)


def refresh_token(path):
    print("Attempting to refresh token at: {}".format(path))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(refresh_token(path))
    print("Token at: {} refreshed.".format(path))


if __name__ == "__main__":
    fire.Fire()

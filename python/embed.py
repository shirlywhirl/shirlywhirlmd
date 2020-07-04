import aiohttp
import asyncio
import fire
import json

from pyfacebook import IgBasicApi


def hello(world="World"):
    """
    Say Hello to fire.
    """
    return "Hello " + world


def _user_by_token(token, count=None):
    """
    Given a user long lived token, generate a list of
    all media posts sorted by newest first.
    """
    api = IgBasicApi(long_term_token=token)
    user = api.get_user_info()
    resp = api.get_user_medias(user_id=user.id, count=count)
    return sorted(resp, key=lambda post: post.timestamp, reverse=True)


async def _get(session, url, media):
    params = {"url": media.permalink, "hidecaption": 0, "omitscript": 1}
    async with session.get(url, params=params) as resp:
        return await resp.text()


async def _embed(token, count=None):
    medias = _user_by_token(token, count=count)
    async with aiohttp.ClientSession() as session:
        for media in medias:
            text = await _get(session, "https://api.instagram.com/oembed", media)
            print(json.loads(text)["html"])


def get_all_html(token):
    """
    Given a long user token spit out all their posts as embedable html
    """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_embed(token))


def get_latest_html(token):
    """
    Given a long user token spit their latest posts as embedable html
    """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_embed(token, count=1))


if __name__ == "__main__":
    fire.Fire()

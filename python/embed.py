import aiohttp
import asyncio
import fire
import json
import time

from post import Post

from pyfacebook import IgBasicApi


def _user_by_token(token, count=None):
    """
    Given a user long lived token, generate a list of
    all media posts sorted by newest first.
    """
    api = IgBasicApi(long_term_token=token)
    user = api.get_user_info()
    resp = api.get_user_medias(user_id=user.id, count=count)
    # trim
    resp = [post for post in resp if post.timestamp >= '2018-12-30' and post.timestamp < '2019-02-14']

    return (sorted(resp, key=lambda post: post.timestamp, reverse=False))


async def _get(session, url, media):
    params = {"url": media.permalink, "hidecaption": 1, "omitscript": 1}
    async with session.get(url, params=params) as resp:
        print(resp.status)
        time.sleep(10)
        return await resp.text()


async def _embed(token, count=None):
    medias = _user_by_token(token, count=count)
    async with aiohttp.ClientSession() as session:
        for media in medias:
            text = await _get(session, "https://api.instagram.com/oembed", media)
            post = Post(media, json.loads(text)["html"] + '\n' + media.caption)
            post.write_jekyll_post()

def get_all_html(token):
    """
    Given a long user token spit out all their posts as embedable html
    """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_embed(token))


def get_last_n_posts(token, n):
    """
    Given a long user token spit their latest posts as embedable html
    """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_embed(token, count=n))


if __name__ == "__main__":
    fire.Fire()

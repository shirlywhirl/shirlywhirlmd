import fire
import aiohttp
import asyncio

from pyfacebook import IgBasicApi

def hello(world = "World"):
    return "Hello " + world

def user_by_token(token):
    '''
    Given a user long lived token, generate a list of
    all media posts sorted by newest first.
    '''
    api = IgBasicApi(long_term_token = token)
    user = api.get_user_info()
    resp = api.get_user_medias(user_id = user.id, count = None)
    return sorted(resp, key=lambda post: post.timestamp, reverse=True)

async def _get(session, url):
    async with session.get(url) as resp:
        return await resp.text()

async def _embed(media_id):
    async with aiohttp.ClientSession() as session:
        html = await _get(session, 'http://python.org')
        print(html)

def get_html(token):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(python())

if __name__ == '__main__':
    fire.Fire()

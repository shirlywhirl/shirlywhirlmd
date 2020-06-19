import aiohttp
import asyncio
import fire
import json

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

async def _get(session, url, media):
    params = { 'url' : media.permalink, 'hidecaption' : 0, 'omitscript' : 1}
    async with session.get(url, params=params) as resp:
        return await resp.text()

async def _embed(token):
    medias = user_by_token(token)
    async with aiohttp.ClientSession() as session:
        for media in medias:
            text = await _get(session, 'https://api.instagram.com/oembed', media)
            print(json.loads(text)['html'])

def get_html(token):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_embed(token))

if __name__ == '__main__':
    fire.Fire()

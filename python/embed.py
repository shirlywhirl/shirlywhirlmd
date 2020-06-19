import fire
import aiohttp

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

if __name__ == '__main__':
    fire.Fire()

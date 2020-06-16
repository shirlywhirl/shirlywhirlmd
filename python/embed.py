import fire
import aiohttp

from pyfacebook import IgBasicApi

def hello(world = "World"):
    return "Hello " + world

def user(token, uid = ''):
    print("Token length: {len}!".format(len=len(token)))
    print("Userid: {uid}".format(uid=uid))
    api = IgBasicApi(long_term_token=token)
    print("Operating as:")
    print(api.get_user_info())
    dir(api)

if __name__ == '__main__':
    fire.Fire()

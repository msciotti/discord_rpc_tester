import requests
from utils import send_and_receive
from constants import TOKEN_URL, RPC_TOKEN_URL_FRAGMENT


async def authorize(ws, client_id, rpc_token):
    payload = {
      'nonce': '12345',
      'args': {
        'client_id': client_id,
        'scopes': ['rpc'],
        'rpc_token': rpc_token
      },
      'cmd': 'AUTHORIZE'
    }
    r = await send_and_receive(ws, payload)
    if r['code'] is not None:
        print('CMD: Authorize - Success!')
        return r['code']
    return


async def authenticate(ws, token):
    payload = {
      'nonce': '12345',
      'args': {
        'access_token': token,
      },
      'cmd': 'AUTHENTICATE'
    }

    r = await send_and_receive(ws, payload)
    if r['application'] is not None:
        print('CMD: Authenticate - Success!')
        return True
    return False


async def subscribe(ws):
    payload = {
      'nonce': '12345',
      'evt': 'GUILD_CREATE',
      'cmd': 'SUBSCRIBE'
    }
    r = await send_and_receive(ws, payload)
    if r['evt'] == 'GUILD_CREATE':
        print('CMD: Subscribe - Success!')
    else:
        print('CMD: Subscribe - Fail!')
    return


async def unsubsribe(ws):
    payload = {
      'nonce': '12345',
      'evt': 'GUILD_CREATE',
      'cmd': 'UNSUBSCRIBE'
    }
    r = await send_and_receive(ws, payload)
    if r['evt'] == 'GUILD_CREATE':
        print('CMD: Unsubscribe - Success!')
    else:
        print('CMD: Unsubscribe - Fail!')
    return


async def run_auth_tests(ws, client_id, client_secret):
    print("Running auth tests...")
    r = requests.post('http://localhost:3000/oauth2/token' + RPC_TOKEN_URL_FRAGMENT,
                      headers={
                        'Content-Type': 'application/x-www-form-urlencoded'
                        },
                      data={
                        'client_id': client_id,
                        'client_secret': client_secret
                      })
    data = r.json()
    print("Got data from rpc token exchange:")
    print(data)
    rpc_token = data['rpc_token']

    code = await authorize(ws, client_id, rpc_token)
    if code is None:
        print('Authorization failed!')
        return False

    r = requests.post('http://localhost:3000/oauth2/token',
                      headers={
                        'Content-Type': 'application/x-www-form-urlencoded'
                      },
                      data={
                        'client_id': client_id,
                        'client_secret': client_secret,
                        'grant_type': 'authorization_code',
                        'code': code
                      })
    data = r.json()
    token = data['access_token']
    print("Got bearer token")
    print(token)
    if not await authenticate(ws, token):
        print('Authentication failed!')
        return False

    await subscribe(ws)
    await unsubsribe(ws)
    return True

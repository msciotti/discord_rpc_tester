import requests
import json
from utils.utils import send_and_receive
from utils.constants import TOKEN_URL, RPC_TOKEN_URL_FRAGMENT, BOT_TOKEN, CLIENT_ID, CLIENT_SECRET, GROUP_DM_URL


async def authorize(ws, client_id, rpc_token):
    payload = {
      'nonce': '12345',
      'args': {
        'client_id': client_id,
        'scopes': ['rpc', 'gdm.join', 'rpc.api'],
        'rpc_token': rpc_token
      },
      'cmd': 'AUTHORIZE'
    }
    r = await send_and_receive(ws, payload)
    return r['code']


async def authenticate(ws, token):
    payload = {
      'nonce': '12345',
      'args': {
        'access_token': token,
      },
      'cmd': 'AUTHENTICATE'
    }

    r = await send_and_receive(ws, payload)
    return r['user']['id']


async def subscribe(ws):
    payload = {
      'nonce': '12345',
      'evt': 'GUILD_CREATE',
      'cmd': 'SUBSCRIBE'
    }
    await send_and_receive(ws, payload)
    return


async def unsubsribe(ws):
    payload = {
      'nonce': '12345',
      'evt': 'GUILD_CREATE',
      'cmd': 'UNSUBSCRIBE'
    }
    await send_and_receive(ws, payload)
    return


def get_rpc_token(client_id, client_secret):
    r = requests.post(TOKEN_URL + RPC_TOKEN_URL_FRAGMENT,
                      headers={
                        'Content-Type': 'application/x-www-form-urlencoded'
                        },
                      data={
                        'client_id': CLIENT_ID,
                        'client_secret': CLIENT_SECRET
                      })
    data = r.json()
    rpc_token = data['rpc_token']
    return rpc_token


def get_bearer_token(code):
    r = requests.post(TOKEN_URL,
                      headers={
                        'Content-Type': 'application/x-www-form-urlencoded'
                      },
                      data={
                        'client_id': CLIENT_ID,
                        'client_secret': CLIENT_SECRET,
                        'grant_type': 'authorization_code',
                        'code': code
                      })
    data = r.json()
    token = data['access_token']
    return token


def create_group_dm(bearer_token, user_id):
    r = requests.post(GROUP_DM_URL,
                      headers={
                        'Authorization': 'Bot ' + BOT_TOKEN
                        },
                      json={
                        'access_tokens': [bearer_token],
                        'nicks': {
                            user_id: 'Please Work Please Work'
                        }
                      })
    group_dm = r.json()
    print('\nTesting Create Group DM Endpoint \nResponse: ' + json.dumps(group_dm, indent=4))
    return group_dm


async def run_auth_tests(ws):
    rpc_token = get_rpc_token(CLIENT_ID, CLIENT_SECRET)
    code = await authorize(ws, CLIENT_ID, rpc_token)
    if code is None:
        print('Authorization failed!')
        return None

    bearer_token = get_bearer_token(code)
    user_id = await authenticate(ws, bearer_token)
    if user_id is None:
        print('Authentication failed!')
        return None

    await subscribe(ws)
    await unsubsribe(ws)
    group_dm = create_group_dm(bearer_token, user_id)
    return user_id, group_dm

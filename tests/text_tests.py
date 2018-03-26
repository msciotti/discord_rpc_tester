import os
from utils.utils import send_and_receive


async def get_guild(ws, id):
    payload = {
      'nonce': '12345',
      'args': {
        'guild_id': id
      },
      'cmd': 'GET_GUILD'
    }
    await send_and_receive(ws, payload)
    return


async def get_guilds(ws):
    payload = {
      'nonce': '12345',
      'args': {},
      'cmd': 'GET_GUILDS'
    }
    r = await send_and_receive(ws, payload)
    return r['guilds'][0]['id']


async def get_channels(ws):
    payload = {
      'nonce': '12345',
      'args': {},
      'cmd': 'GET_CHANNELS'
    }
    r = await send_and_receive(ws, payload)
    return r['channels'][0]['id']


async def get_channel(ws, id):
    payload = {
      'nonce': '12345',
      'args': {
        'channel_id': id
      },
      'cmd': 'GET_CHANNEL'
    }
    await send_and_receive(ws, payload)
    return


async def select_text_channel(ws, channel_id):
    payload = {
      'nonce': '12345',
      'args': {
        'channel_id': channel_id
      },
      'cmd': 'SELECT_TEXT_CHANNEL'
    }
    await send_and_receive(ws, payload)
    return


async def set_activity(ws):
    payload = {
      'nonce': '12345',
      'args': {
        'pid': os.getpid(),
        'activity': {
          'state': 'Testing',
          'details': 'Running the RPC tester'
        }
      }
    }
    await send_and_receive(ws, payload)
    return


async def run_text_tests(ws):
    channel_id = await get_channels(ws)
    await get_channel(ws, channel_id)
    guild_id = await get_guilds(ws)
    await get_guild(ws, guild_id)
    await set_activity(ws)
    return

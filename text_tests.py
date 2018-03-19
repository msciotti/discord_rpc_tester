from utils import send_and_receive


async def get_guild(ws, id):
    payload = {
      'nonce': '12345',
      'args': {
        'guild_id': id
      },
      'cmd': 'GET_GUILD'
    }
    r = await send_and_receive(ws, payload)
    if r['name'] is not None:
        print('CMD: Get Guild - Success!')
    else:
        print('CMD: Get Guild - Fail!')
    return


async def get_guilds(ws):
    payload = {
      'nonce': '12345',
      'args': {},
      'cmd': 'GET_GUILDS'
    }
    r = await send_and_receive(ws, payload)
    if r['guilds'][0]['id'] is not None:
        print('CMD: Get Guilds - Success!')
        await get_guild(ws, r['guilds'][0]['id'])
    else:
        print('CMD: Get Guilds - Fail!')
        print('CMD: Get Guild - Fail!')
    return


async def get_channels(ws):
    payload = {
      'nonce': '12345',
      'args': {},
      'cmd': 'GET_CHANNELS'
    }
    r = await send_and_receive(ws, payload)
    if r['channels'][0]['id'] is not None:
        print('CMD: Get Channel - Success!')
        await select_text_channel(ws, r['channels'][0]['id'])
    else:
        print('CMD: Get Channels - Fail!')
        print('CMD: Get Channel - Fail!')
    return


async def get_channel(ws, id):
    payload = {
      'nonce': '12345',
      'args': {
        'guild_id': id
      },
      'cmd': 'GET_CHANNEL'
    }
    r = await send_and_receive(ws, payload)
    if r['name'] is not None:
        print('CMD: Get Channel - Success!')
    else:
        print('CMD: Get Channel - Fail!')
    return


async def select_text_channel(ws, channel_id):
    payload = {
      'nonce': '12345',
      'args': {
        'channel_id': channel_id
      },
      'cmd': 'SELECT_TEXT_CHANNEL'
    }
    r = await send_and_receive(ws, payload)
    if r['id'] is not None:
        print('CMD: Select Text Channel - Success!')
    else:
        print('CMD: Select Text Channel - Fail!')
    return


async def run_text_tests(ws):
    await get_channels(ws)
    await get_guilds(ws)
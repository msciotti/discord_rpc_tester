from utils.utils import send_and_receive
from utils.constants import CLIENT_ID


async def select_voice_channel(ws, channel_id):
    payload = {
      'nonce': '1245',
      'args': {
        'channel_id': channel_id,
        'force': True
      },
      'cmd': 'SELECT_VOICE_CHANNEL'
    }
    await send_and_receive(ws, payload)
    return


async def get_selected_voice_channel(ws):
    payload = {
      'nonce': '12345',
      'args': {},
      'cmd': 'GET_SELECTED_VOICE_CHANNEL'
    }
    await send_and_receive(ws, payload)
    return


async def set_voice_settings(ws):
    payload = {
      'nonce': '1245',
      'args': {
        'mode': {
          'type': 'VOICE_ACTIVITY'
        }
      },
      'cmd': 'SET_VOICE_SETTINGS'
    }
    await send_and_receive(ws, payload)
    return


async def capture_shortcut(ws):
    payload = {
      'nonce': '12345',
      'args': {
        'action': 'START'
      },
      'cmd': 'CAPTURE_SHORTCUTE'
    }
    await ws.send(payload)
    print('Enter three key combos for PTT shortcuts')
    more = 3
    while more > 0:
        r = await ws.receive()
        print(r['shortcut'])
        more -= 1
    return


async def get_voice_settings(ws):
    payload = {
      'nonce': '1245',
      'args': {},
      'cmd': 'GET_VOICE_SETTINGS'
    }
    await send_and_receive(ws, payload)
    return


async def set_certified_devices(ws):
    payload = {
        'nonce': '12345',
        'args': {
            'devices': [{
                'type': 'audioinput',
                'id': CLIENT_ID,
                'vendor': {
                    'name': 'SteelSeries',
                    'url': 'https://steelseries.com'
                },
                'model': {
                    'name': 'Arctis 7',
                    'url': 'https://steelseries.com/gaming-headsets/arctis-7'
                },
                'related': ['Arctis 5 - Dota 2 Limited Edition'],
                'echo_cancellation': False,
                'noise_suppression': False,
                'automatic_gain_control': False,
                'hardware_mute': False
            }]
        },
        'cmd': 'SET_CERTIFIED_DEVICES'
    }
    await send_and_receive(ws, payload)
    return


async def run_voice_tests(ws, voice_channel_id, user_id):
    await set_certified_devices(ws)
    await select_voice_channel(ws, voice_channel_id)
    await get_selected_voice_channel(ws)
    await get_voice_settings(ws)
    await set_voice_settings(ws)
    await select_voice_channel(ws, None)

async def set_user_voice_settings(ws):
    payload = {
      'nonce': '12345',
      'args': {
        'user_id': user_id,
        'pan': {
          'left': 1.0,
          'right': 1.0
        },
        'volume': 120,
        'mute': True
      },
      'cmd': 'SET_USER_VOICE_SETTINGS'
    }
    r = await send_and_receive(ws, payload)
    if r['mute'] is True:
        print('CMD: Set User Voice Settings: Success!'
    else:
        print('CMD: Set User Voice Settings: Fail!'
    return


async def select_voice_channel(ws, channel_id):
    payload = {
      'nonce': '1245',
      'args': {
        'channel_id': channel_id
      },
      'cmd': 'SELECT_VOICE_CHANNEL'
    }
    r = await send_and_receive(ws, payload)
    if r['id'] is not None:
        print('CMD: Select Voice Channel - Success!'
    else:
        print('CMD: Select Voice Channel - Fail!'
    return


async def get_selected_voice_channel(ws):
    payload = {
      'nonce': '12345',
      'args': {},
      'cmd': 'GET_SELECTED_VOICE_CHANNEL'
    }
    r = await send_and_receive(ws, payload)
    if r['id'] is not None:
        print('CMD: Get Selected Voice Channel - Success!'
    else:
        print('CMD: Get Selected Voice Channel - Fail!'
    return


async def set_voice_settings(ws):
    payload = {
      'nonce': '1245':
      'args': {
        'mode': {
          'type': 'VOICE_ACTIVITY'
        }
      },
      'cmd': 'SET_VOICE_SETTINGS'
    }
    r = await send_and_receive(ws, payload)
    if r['mode']['type'] == 'VOICE_ACTIVITY':
        print('CMD: Set Voice Settings - Success!'
    else:
        print('CMD: Set Voice Settings - Fail!'
    return


async def capture_shortcut(ws):
    payload = {
      'nonce': '12345':
      'args': {
        'action': 'START'
      },
      'cmd': 'CAPTURE_SHORTCUTE'
    }
    await ws.send(payload)
    print('Enter three key combos for PTT shortcuts'
    more = 3
    while more > 0:
        r = await ws.receive()
        print r['shortcut']
        more -= 1
    return


async def get_voice_settings(ws):
    payload = {
      'nonce': '1245':
      'args': {},
      'cmd': 'GET_VOICE_SETTINGS'
    }
    r = await send_and_receive(ws, payload)
    if r['mode'] is not None:
        print('CMD: Get Voice Settings - Success!'
    else:
        print('CMD: Get Voice Settings - Fail!'
    return

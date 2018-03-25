import json


async def send_and_receive(ws, payload):
    print('\nTesting {} \nResponse: '.format(payload['cmd']))
    s = json.dumps(payload, indent=4)
    await ws.send(s)
    r = await ws.recv()
    d = json.loads(r)
    print(json.dumps(d, indent=4))
    return d['data']

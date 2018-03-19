import json


async def send_and_receive(ws, payload):
    s = json.dumps(payload)
    print("Sending payload")
    print(payload)
    await ws.send(s)
    r = await ws.recv()
    d = json.loads(r)
    print(d)
    return d['data']

import websockets
import asyncio
from auth_tests import run_auth_tests
from text_tests import run_text_tests
# from voice_tests import run_voice_tests
from constants import RPC_HOSTNAME, RPC_QUERYSTRING, CLIENT_ID, RPC_ORIGIN, CLIENT_SECRET


async def test():
    print(""" Welcome to the Discord RPC Tester!
          Let's make sure we didn't break anything... """)

    port = input('Enter the port to connect to: ')
    # client_id = input('Enter the client_id of your application: ')
    # client_secret = input('Enter the client_secret of your application: ')
    uri = RPC_HOSTNAME + port + RPC_QUERYSTRING + CLIENT_ID
    print("Opening connection to {}".format(uri))
    async with websockets.connect(uri, origin=RPC_ORIGIN) as ws:
        print('Connected! Let\'s begin:\n')
        r = await ws.recv()
        print(r)
        if await run_auth_tests(ws, CLIENT_ID, CLIENT_SECRET):
            await run_text_tests(ws)
            # run_voice_tests(ws)
            print('Yay! Tests completed!')
        else:
            print('Could not connect to RPC. Stopping')
        return


asyncio.get_event_loop().run_until_complete(test())

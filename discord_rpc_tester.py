import websockets
import asyncio
from tests.auth_tests import run_auth_tests
from tests.text_tests import run_text_tests
from tests.voice_tests import run_voice_tests
from utils.constants import RPC_HOSTNAME, RPC_QUERYSTRING, CLIENT_ID, RPC_ORIGIN


async def test():
    print("Welcome to the Discord RPC Tester!")
    print("Let's make sure we didn't break anything...\n")

    port = input('Enter the port to connect to: ')
    uri = RPC_HOSTNAME + port + RPC_QUERYSTRING + CLIENT_ID
    print("Opening connection to {}".format(uri))
    async with websockets.connect(uri, origin=RPC_ORIGIN) as ws:
        print('Connected! Let\'s begin:\n')
        r = await ws.recv()
        print(r)
        user_id, group_dm = await run_auth_tests(ws)
        if user_id is not None:
            await run_text_tests(ws)
            await run_voice_tests(ws, group_dm['id'], user_id)
            print('Yay! Tests completed!')
        else:
            print('Could not connect to RPC. Stopping')
        return


asyncio.get_event_loop().run_until_complete(test())

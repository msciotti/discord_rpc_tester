# discord_rpc_tester

This script and series of tests can be used for testing the suite of RPC commands against a local client, or the GameBridge SDK to ensure that they all function properly.

## Steps

1. Clone the repo
2. Go to [your Discord applications](https://discordapp.com/developers/applications/me) and find your RPC-whitelisted application
3. Make sure you create a bot user for your application, as you will need the Bot token for the token exchange
4. Copy the necessary information into `utils/constants.py`
5. Run the script, inputting the port number at which the SDK or local client is listening. For local clients, open the console and search at the start of the logs for the port number. For the GameBridge SDK, input the port number returned from the initialize callback.

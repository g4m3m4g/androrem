from ppadb.client import Client as AdbClient

client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()

if not devices:
    raise RuntimeError("No devices connected")

device = devices[0]

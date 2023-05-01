import asyncio
from bleak import BleakScanner, BleakClient


async def connect_to_device(device_address):
    async with BleakClient(device_address) as client:
        # Connection successful, do something with the client
        print(f"Connected to {device_address}")

        # Read/write/subscribe to characteristics or perform other operations

        # Disconnect when done
        await client.disconnect()
        print(f"Disconnected from {device_address}")


async def main():
    scanner = BleakScanner()
    devices = await scanner.discover()

    # Print the list of discovered devices
    for device in devices:
        print(f"Found device: {device}")

    # Connect to a specific device by address
    target_device_address = "<device_address>"  # Replace with the address of the device you want to connect to

    if target_device_address in devices:
        await connect_to_device(target_device_address)
    else:
        print("Device not found")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

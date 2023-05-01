import bluetooth

# Get a list of already paired devices
paired_devices = bluetooth.discover_devices()

# Print the list of paired devices
for device_addr in paired_devices:
    device_name = bluetooth.lookup_name(device_addr)
    print(f"Found device: {device_name} ({device_addr})")

# Connect to a specific device by address
target_device = "<device_address>"  # Replace with the address of the device you want to connect to

if target_device in paired_devices:
    try:
        socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        socket.connect((target_device, 1))  # Use the appropriate port number for your device

        # Connection successful, do something with the socket

        # Close the socket when done
        socket.close()

    except bluetooth.BluetoothError as e:
        print(f"Error occurred while connecting: {str(e)}")
else:
    print("Device not found in paired devices.")

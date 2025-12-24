import asyncio
from bleak import BleakScanner

seen_devices = set()


def detection_callback(device, advertisement_data):
    name = advertisement_data.local_name or device.name

    # Ignore devices without a name
    if not name:
        return

    # Ignore already seen devices
    if device.address in seen_devices:
        return

    seen_devices.add(device.address)

    print(f"Name: {name}")
    print(f"Address: {device.address}")
    print("-" * 30)


async def scan():
    print("Scanning for BLE devices...")
    scanner = BleakScanner(detection_callback)

    await scanner.start()
    await asyncio.sleep(8)
    await scanner.stop()


asyncio.run(scan())

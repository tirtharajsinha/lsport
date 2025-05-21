import os
import argparse

try:
    from tabulate import tabulate
    tabulate_available = True
except ImportError:
    tabulate_available = False


def find_serial_devices(raw_paths=False):
    by_id_path = "/dev/serial/by-id/"
    devices = []

    if not os.path.exists(by_id_path):
        raise FileNotFoundError("No Serial device found. Is your serial device plugged in?")

    for entry in os.listdir(by_id_path):
        full_link = os.path.join(by_id_path, entry)
        if os.path.islink(full_link):
            target = os.readlink(full_link)
            if not raw_paths:
                # Resolve ../../ to /dev path
                target = os.path.realpath(full_link)
            devices.append((entry, target))

    return devices


def main():
    parser = argparse.ArgumentParser(description="List serial devices by ID")
    parser.add_argument("--no-table", action="store_true", help="Do not format output as a table")
    parser.add_argument("--raw", action="store_true", help="Show raw symlink paths instead of full /dev path")
    args = parser.parse_args()

    try:
        devices = find_serial_devices(raw_paths=args.raw)
    except Exception as e:
        print(f"{e}")
        return

    if not devices:
        print("No serial devices found.\n")
        print("Tip: Try running `lsusb -t` to check if drivers are installed.")
        return

    use_table = tabulate_available and not args.no_table

    if use_table:
        print()
        print(tabulate(devices, headers=["Device Name", "Port"]))
        print()
    else:
        print("Device Name\t -> Port")
        print("------------\t -----------")
        for name, path in devices:
            print(f"{name}\t -> {path}")

    print(f"\n{len(devices)} device{'s' if len(devices) != 1 else ''} found.\n")



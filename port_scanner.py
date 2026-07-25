import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
from banner import banner


open_ports = []


def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((host, port))

        if result == 0:
            open_ports.append(port)
            print(f"[OPEN] Port {port}")

        sock.close()

    except Exception:
        pass


def main():

    banner()

    parser = argparse.ArgumentParser(
        description="Simple TCP Port Scanner"
    )

    parser.add_argument(
        "host",
        help="Target Host or IP Address"
    )

    parser.add_argument(
        "-s",
        "--start",
        type=int,
        default=1,
        help="Start Port"
    )

    parser.add_argument(
        "-e",
        "--end",
        type=int,
        default=1024,
        help="End Port"
    )

    parser.add_argument(
        "-t",
        "--threads",
        type=int,
        default=100,
        help="Number of Threads"
    )

    args = parser.parse_args()

    print("=" * 40)
    print(f"Target : {args.host}")
    print(f"Ports  : {args.start} - {args.end}")
    print("=" * 40)

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(
            lambda port: scan_port(args.host, port),
            range(args.start, args.end + 1)
        )

    print("\nScan Completed!")

    if len(open_ports) == 0:
        print("No open ports found.")
    else:
        print(f"\nTotal Open Ports : {len(open_ports)}")


if __name__ == "__main__":
    main()

import socket


COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]


def scan_port(host: str, port: int, timeout: float = 0.5) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        result = sock.connect_ex((host, port))
        return result == 0
    except socket.error:
        return False
    finally:
        sock.close()


def run_port_scanner() -> None:
    host = input("Enter target host or IP: ").strip()
    print(f"Scanning common ports on {host}...\n")

    open_ports = []
    for port in COMMON_PORTS:
        if scan_port(host, port):
            open_ports.append(port)
            print(f"[OPEN] Port {port}")
        else:
            print(f"[CLOSED] Port {port}")

    print("\nScan complete.")
    if open_ports:
        print("Open ports found:", ", ".join(map(str, open_ports)))
    else:
        print("No open common ports found.")

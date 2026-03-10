import psutil


def bytes_to_mb(value: int) -> float:
    return value / (1024 * 1024)


def run_network_monitor() -> None:
    net_io = psutil.net_io_counters()
    connections = psutil.net_connections(kind="inet")

    print("=== Network Usage ===")
    print(f"Bytes sent: {bytes_to_mb(net_io.bytes_sent):.2f} MB")
    print(f"Bytes received: {bytes_to_mb(net_io.bytes_recv):.2f} MB")

    print("\n=== Active Connections ===")
    if not connections:
        print("No active connections found.")
        return

    shown = 0
    for conn in connections:
        local_addr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
        remote_addr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
        status = conn.status
        pid = conn.pid

        print(f"Local: {local_addr} | Remote: {remote_addr} | Status: {status} | PID: {pid}")
        shown += 1

        if shown >= 15:
            print("\nShowing first 15 connections only.")
            break

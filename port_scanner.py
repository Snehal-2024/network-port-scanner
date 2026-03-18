import socket
import threading
from datetime import datetime

print("="*50)
print("        NETWORK PORT SCANNER")
print("="*50)

target = input("Enter target IP or domain: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid target")
    exit()

print(f"\nScanning Target: {target} ({target_ip})")
print("Scanning started at:", datetime.now())
print("-"*50)

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

def scan_port(port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target_ip, port))

    if result == 0:
        service = common_ports.get(port, "Unknown Service")
        print(f"[OPEN] Port {port} - {service}")

    scanner.close()


threads = []

for port in range(1, 1025):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("-"*50)
print("Scanning completed at:", datetime.now())
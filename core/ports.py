import socket
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

COMMON_PORTS = [21, 22, 80, 443, 3306, 8080]

def check_port(host, port):
    s = socket.socket()
    s.settimeout(0.4)
    try:
        s.connect((host, port))
        return port
    except:
        return None
    finally:
        s.close()

def port_scan(url):
    print("[*] Scanning ports...")

    host = urlparse(url).netloc

    open_ports = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(lambda p: check_port(host, p), COMMON_PORTS)

    for r in results:
        if r:
            print(f"[+] Port {r} OPEN")
            open_ports.append(r)

    return open_ports
import socket
import datetime

def scan_port(host, port):
    try:
        socket.create_connection((host, port), timeout=0.5)
        return True
    except:
        return False
    
def scan_range(host, start_port, end_port):
    open_ports =[]
    for port in range (start_port, end_port +1):
        if scan_port(host, port):
            open_ports.append(port)
    return open_ports

def port_scanner_report(host, start_port, end_port):
    if start_port > end_port:
        print (f"Error: start_port cannot be greater than end_port")
        return
    if start_port < 1 or end_port > 65535:
        print (f"Error: port range 1-65535")
        return
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    results = scan_range(host, start_port, end_port)
    print(f"Port Scanner Report")
    print("-------------------")
    print(f"Scan Time: {timestamp}")
    print(f"Host: {host}")
    print(f"Ports Scanned: {start_port} - {end_port}")
    for port in results:
        print(f"Port {port} --- Open")
    with open("scan_log.txt", "a") as log:
        log.write(f"\{timestamp}\n")
        log.write(f"Host: {host}\n")
        log.write(f"ports Scanned: {start_port} - {end_port}\n")
        for port in results:
            log.write(f"Port {port} --- Open\n")
            log.write("---------------\n")
    return results
    
port_scanner_report("google.com", 0, 85)

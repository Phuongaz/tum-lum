import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) 
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()
    except socket.error:
        print(f"Error occurred while scanning port {port}")

host = input("Enter the host to scan: ")
ports = [int(port) for port in input("Enter the ports to scan: ").split(",")]

for port in ports:
    scan_port(host, port)
import ssl
import socket

def validate_certificate(host, port):
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as secure_sock:
            cert = secure_sock.getpeercert()
            
            trusted = cert.get('issuer') and cert.get('issuer')[0][0][1] == 'commonName' and \
                      cert.get('issuer')[0][0][1] == cert.get('subject')[0][0][1]

            return trusted

host = input("Enter the host to validate: ")
port = int(input("Enter the port to validate: "))
trusted = validate_certificate(host, port)
if trusted:
    print(f"The certificate for {host} is trusted.")
else:
    print(f"The certificate for {host} is not trusted.")
import ssl
import socket
from datetime import datetime

def check_cert(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

        not_after = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
        
        if datetime.utcnow() > not_after:
            return False
        else:
            return True

    except Exception as e:
        return False
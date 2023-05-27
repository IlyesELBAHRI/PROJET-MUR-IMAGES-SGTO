import sys
import paramiko
from scp import SCPClient

def create_ssh_client(server: str, port: int, user: str, password: str) -> paramiko.SSHClient:
    """
    Create an SSH client and connect to the specified server.

    Args:
        server: The hostname or IP address of the server to connect to.
        port: The port number to use for the SSH connection.
        user: The username to use for the SSH connection.
        password: The password to use for the SSH connection.

    Returns:
        An instance of `paramiko.SSHClient` connected to the specified server.
    """

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client


def is_valid_ip_address(ip_address: str) -> bool:
    """
    Check if the specified string is a valid IP address.

    Args:
        ip_address: The string to check.

    Returns:
        True if the string is a valid IP address, False otherwise.
    """

    parts = ip_address.split('.')

    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        
        num = int(part)

        if num < 0 or num > 255:
            return False
        
    return True


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("Usage: python scp_bleep.py <server> <port> <user> <password>")
        sys.exit(1)

    server = sys.argv[1]
    port = int(sys.argv[2])
    user = sys.argv[3]
    password = sys.argv[4]

    if is_valid_ip_address(ip_address=server):
        with create_ssh_client(server=server, port=port, user=user, password=password) as ssh:
            if transport := ssh.get_transport():
                SCPClient(transport).put('scp_bleep.py', '/home/nvidia/appli/', recursive=True)
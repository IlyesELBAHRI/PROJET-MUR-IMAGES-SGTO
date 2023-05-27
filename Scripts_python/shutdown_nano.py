import paramiko as pmk

NANOS = 2
NANOS_BASE_IP = "192.168.1.20"

ssh = pmk.SSHClient()

for i in range(1, NANOS+1):
    ip = NANOS_BASE_IP + str(i)
    print("ssh to " + ip)

    try:
        ssh.set_missing_host_key_policy(pmk.AutoAddPolicy())
        ssh.connect(ip, username=f"slave{i}", password="slave123")
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(
            "sudo shutdown -h now")
    except:
        print("Failed to connect to " + ip)

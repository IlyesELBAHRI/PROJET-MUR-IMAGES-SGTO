import paramiko as pmk

RPIS = 9
RPIS_BASE_IP = "192.168.1.10"

ssh = pmk.SSHClient()

for i in range(1, RPIS+1):
    ip = RPIS_BASE_IP + str(i)
    print("ssh to " + ip)

    try:
        ssh.set_missing_host_key_policy(pmk.AutoAddPolicy())
        ssh.connect(ip, username="pi", password="slave123", timeout=5)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(
            "sudo shutdown -h now")
    except:
        print("Failed to connect to " + ip)

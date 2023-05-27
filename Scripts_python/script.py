import time
import subprocess

command_meteo = "sudo python3 /home/nvidia/appli/meteo.py"

command_ratp = "sudo python3 /home/nvidia/appli/ratp.py"

command_date = "sudo python3 /home/nvidia/appli/date.py"

command_site = "sudo python3 /home/nvidia/appli/site/v1.py"

time.sleep(10)

subprocess.run(command_date, shell=True)
subprocess.Popen(command_site, shell=True)
subprocess.Popen(command_meteo, shell=True)

while True:
    subprocess.Popen(command_ratp, shell=True)
    time.sleep(30) 

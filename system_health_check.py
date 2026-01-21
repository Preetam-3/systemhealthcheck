
import subprocess
import smtplib
import schedule
from email.message import EmailMessage
import time

cpu_usage = subprocess.check_output("top -b -n2 | grep 'Cpu(s)' | tail -1 | awk '{print 100 - $8}'", shell=True).decode('utf-8').strip()
print(f"CPU Usage: {cpu_usage}%")
ram_usage = subprocess.check_output("vmstat -s | awk 'NR==1{total=$1} NR==2{used=$1; printf \"%.2f\", (used/total)*100}'",shell=True).decode('utf-8').strip()
print(f"Ram Usage: {ram_usage}")
disk_usage = subprocess.check_output("df --block-size=1K | awk 'NR>1 && !/tmpfs|devtmpfs/ {u += $3; t += $2} END {printf \"%.1f\\n\", (u/t)*100}'", shell=True).decode('utf-8').strip()                
print(f"Disk Usage: {disk_usage}")

cpu = float(cpu_usage)
ram = float(ram_usage)
disk = float(disk_usage)
code = "" 
count = 0
def health(x):
    if  x > 90.00:
        return "Critical"
    elif 70.00 < x < 90.00:
        return "Warning"
    else: 
        return "Ok"


if health(cpu) != "Ok": 
    code += 'cpu'
if health(ram) != "Ok": 
    code += 'ram'
elif health(disk) != "Ok": 
    code += 'disk'


def switch(code):
    if code == 'cpu':
        return 'Your Cpu is is getting full'
    elif code == 'cpuram':
        return 'Your Ram and Cpu is getting full'
    elif code == 'cpuramdisk':
        return 'Your Cpu,Ram and Disk is getting full'
    elif code == 'ram':
        return 'Your ram is getting full'
    elif code == 'ramdisk':
        return 'Your Ram and disk is getting full'
    elif code == 'disk':
        return 'Your disk is getting full'

if code != '': 
    msg = EmailMessage()
    msg.set_content(switch(code))
    msg["Subject"] = "Sytem Alert: System Warning"
    msg["From"] = "preetambadatya16@gmail.com"
    msg["to"] = "shulong16@proton.me"
    print("Enter your Gmail app password: ")
    pssd = input()
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('preetambadatya16@gmail.com', pssd)

            print("Email sent succesfully")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("All system are normal.No email")

























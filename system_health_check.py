import subprocess
import smtplib
import schedule
from email.message import EmailMessage
import time

timer = int(input(f"For how much time you want to run the process "))


counts = {
    'cpu': 0, 
    'ram': 0, 
    'disk': 0, 
    'cpuram': 0,
    'ramdisk': 0, 
    'cpuramdisk': 0
}
alert_message = ""

def usagechecker():
    global alert_message

    cpu_usage = subprocess.check_output("top -b -n2 | grep 'Cpu(s)' | tail -1 | awk '{print 100 - $8}'", shell=True).decode('utf-8').strip()
    # print(f"CPU Usage: {cpu_usage}%")
    ram_usage = subprocess.check_output("vmstat -s | awk 'NR==1{total=$1} NR==2{used=$1; printf \"%.2f\", (used/total)*100}'",shell=True).decode('utf-8').strip()
    # print(f"Ram Usage: {ram_usage}")
    disk_usage = subprocess.check_output("df --block-size=1K | awk 'NR>1 && !/tmpfs|devtmpfs/ {u += $3; t += $2} END {printf \"%.1f\\n\", (u/t)*100}'", shell=True).decode('utf-8').strip()                
    # print(f"Disk Usage: {disk_usage}")
    

    cpu = float(cpu_usage)
    ram = float(ram_usage)
    disk = float(disk_usage)

    def health(x):
        if  x > 90.00:
            return "Critical"
        elif 70.00 < x < 90.00:
            return "Warning"
        else: 
            return "Ok"

    print(f"Status: CPU: {cpu}% RAM: {ram}% Disk: {disk}%")


    code = ""
    if health(cpu) != "Ok": 
        code += 'cpu'
    if health(ram) != "Ok": 
        code += 'ram'
    elif health(disk) != "Ok": 
        code += 'disk'
   

    if code in counts:
        counts[code] += 1
        if counts[code] == timer:
            messagge = {
                 'cpu': 'Your Cpu is getting full',
                'ram': 'Your Ram is getting full',
                'disk': 'Your Disk is getting full',
                'cpuram': 'Your Ram and Cpu are getting full',
                'ramdisk': 'Your Ram and Disk are getting full',
                'cpuramdisk': 'Your Cpu, Ram and Disk are getting full'
            }
            alert_message = messagge.get(code)

schedule.every(1).seconds.do(usagechecker)

end = time.time() + timer
while time.time() < end:
    schedule.run_pending()
    time.sleep(1)

if alert_message != '': 
    msg = EmailMessage()
    msg.set_content(alert_message)
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

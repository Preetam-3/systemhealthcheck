import subprocess
import smtplib
import schedule
from email.message import EmailMessage
import time

print("This process will run for 15 sec")
timer = 15

counts = {
    'cpu': 0, 
    'ram': 0, 
    'disk': 0, 
    'cpuram': 0,
    'ramdisk': 0, 
    'cpuramdisk': 0
}
alert_message = ""
THRESHOLD = 4

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
    if health(disk) != "Ok": 
        code += 'disk'

    for k in counts:
        if k != code:
            counts[k] = 0
    if code:
        counts[code] += 1

        if counts[code] == THRESHOLD:
            message = {               
                'cpu': 'Your CPU usage is high',
                'ram': 'Your RAM usage is high',
                'disk': 'Your Disk usage is high',
                'cpuram': 'Your CPU and RAM usage are high',
                'ramdisk': 'Your RAM and Disk usage are high',
                'cpuramdisk': 'Your CPU, RAM and Disk usage are high'

            }
            alert_message = message.get(code)

schedule.every(1).seconds.do(usagechecker)

end = time.time() + timer
while time.time() < end:
    schedule.run_pending()
    time.sleep(1)

if alert_message != '': 
    msg = EmailMessage()
    msg.set_content(alert_message)
    toemail = input("Enter receipeint email: ")
    msg["Subject"] = "System Alert: System Warning"
    msg["From"] = "preetambadatya16@gmail.com"
    msg["to"] = toemail 

    pssd = input("Enter you Gmail App password: ")
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('preetambadatya16@gmail.com', pssd)
            smtp.send_message(msg)

            print("Email sent succesfully")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("All system are normal.No email sent")

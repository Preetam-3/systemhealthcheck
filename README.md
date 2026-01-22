# systemhealthcheck
Check the health of the system and sends an alert when system goes down.

 System Health Monitor & Alerter
A lightweight Python script that monitors CPU, RAM, and Disk usage for a user-defined duration. If system resources exceed health thresholds (70% for Warning, 90% for Critical), it automatically sends a detailed alert email.
Features
    • Cross-Platform Support: Works on Linux, macOS, and Windows (with WSL or Git Bash).
    • Real-time Monitoring: Prints system status to the terminal every second.
    • Intelligent Alerting: Combines multiple resource warnings (e.g., "CPU and RAM are full") into a single notification.
    • Configurable Duration: Choose exactly how long you want to monitor the system.

 Prerequisites
    1. Python 3.x: Ensure Python is installed on your machine.
    2. Dependencies: Install the required scedule library:
       Bash
       pip install schedule
    3. Gmail App Password: For security, Gmail requires an App Password rather than your regular login password.
        ◦ Go to your Google Account Settings.
        ◦ Enable 2-Step Verification.
        ◦ Search for App Passwords and generate one for "Mail."

 Installation & Setup
1. Clone the Repository
Bash
git clone https://github.com/your-username/system-monitor.git
cd system-monitor
2. Configure Email Settings
Open the script and update the following lines with your details:
    • msg["From"] = "your-email@gmail.com"
    • msg["To"] = "receiver-email@proton.me"

Usage
Run the script from your terminal:
Bash
python my_process.py
    1. Input Duration: The script will ask: For how much time you want to run the process. Enter the time in seconds (e.g., 60).
    2. Monitor: The terminal will display live status updates.
    3. Authenticate: If a warning threshold is met during the session, you will be prompted to enter your Gmail App Password at the end to send the alert.

- Cross-Platform Support: Works on Linux, macOS, and Windows (with WSL or Git Bash).
- Real-time Monitoring: Prints system status to the terminal every second.
- Intelligent Alerting: Combines multiple resource warnings (e.g., "CPU and RAM are full") into a single notification.
- Configurable Duration: Choose exactly how long you want to monitor the system.
## Prerequisties

- Python 3.x: Ensure Python is installed on your machine.
- Dependencies: Install the required schedule library:
```Bash
pip install schedule
```

- Gmail App Password: For security, Gmail requires an App Password rather than your regular login password.
- Go to your Google Account Settings.
- Enable 2-Step Verification.
- Search for App Passwords and generate one for "Mail."Run the script from your terminal:
```
python my_process.py
```
- Input Duration: The script will ask: For how much time you want to run the process. Enter the time in seconds (e.g., 60).
- Monitor: The terminal will display live status updates.
- Authenticate: If a warning threshold is met during the session, you will be prompted to enter your Gmail App Password at the end to send the alert.

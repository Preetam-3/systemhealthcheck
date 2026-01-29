
# 🩺 System Health Monitor & Alerter

A **lightweight, cross-platform Python system monitoring tool** that continuously checks **CPU, RAM, and Disk usage** and sends an **email alert** when the system becomes unhealthy.

If resource usage crosses defined thresholds, the tool intelligently summarizes the issue and notifies you — no noise, no spam.

---

## 🚀 What This Tool Does 

* Watches your **CPU, Memory, and Disk usage every second**
* Categorizes system health into:

  * 🟡 **Warning** → usage ≥ 70%
  * 🔴 **Critical** → usage ≥ 90%
* Combines multiple issues into **one clean alert**

  * Example: *"CPU and RAM usage are critical"*
* Sends a **single email alert** after monitoring completes
* Runs for **exactly the duration you choose**

This is meant to be **simple, transparent, and predictable** — not an over-engineered monitoring stack.

---

## ✨ Features

* ✅ **Cross-Platform**
  Works on **Linux**, **macOS**, and **Windows** (via WSL or Git Bash)

* ⏱ **Real-Time Monitoring**
  Prints live system health to the terminal **every second**

* 🧠 **Intelligent Alerting**
  Groups multiple resource issues into a **single meaningful email**

* ⚙️ **User-Controlled Duration**
  Decide how long the monitoring should run (in seconds)

---

## 📦 Prerequisites

### 1️⃣ Python

* Python **3.x** must be installed
* Verify with:

```bash
python --version
```

---

### 2️⃣ Required Dependency

Install the `schedule` library:

```bash
pip install schedule
```

---

### 3️⃣ Gmail App Password 

Gmail **does not allow normal passwords** for SMTP anymore.
You must generate an **App Password**.

**Steps:**

1. Go to **Google Account Settings**
2. Enable **2-Step Verification**
3. Search for **App Passwords**
4. Generate one for **Mail**
5. Save it — you’ll enter it when prompted by the script

---

## 📥 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/system-monitor.git
cd system-monitor
```

---

### 2️⃣ Configure Email Settings

Open the Python script (`my_process.py`) and update the email fields:

```python
msg["From"] = "your-email@gmail.com"
msg["To"] = "receiver-email@proton.me"
```

⚠️ **Do NOT hardcode your Gmail password.**
The script will ask for the **App Password only if an alert is needed**.

---

## ▶️ Usage

Run the script from your terminal:

```bash
python my_process.py
```

### What Happens Next?

1️⃣ **Input Duration**
You’ll be asked:

```
For how much time you want to run the process (in seconds):
```

Example:

```
60
```

---

2️⃣ **Live Monitoring**
Every second, the terminal prints:

* CPU usage
* RAM usage
* Disk usage
* Health status (Normal / Warning / Critical)

---

3️⃣ **Email Authentication (Only If Needed)**

* If **any warning or critical threshold** is reached during monitoring:

  * You’ll be prompted **once** at the end
  * Enter your **Gmail App Password**
  * A **single alert email** is sent

If the system stays healthy → **no email is sent**.

---

## 📊 Threshold Logic

| Resource | Warning | Critical |
| -------- | ------- | -------- |
| CPU      | ≥ 70%   | ≥ 90%    |
| RAM      | ≥ 70%   | ≥ 90%    |
| Disk     | ≥ 70%   | ≥ 90%    |

---

## 🧠 Alert Intelligence

Instead of spamming multiple emails, the script:

* Tracks **all resource breaches**
* Merges them into **one concise message**

**Example Email Subject:**

```
System Alert: CPU and RAM Critical
```

---

## 🛡 Security Notes 

* ✅ App Passwords are **safer than normal Gmail passwords**
* ❌ Never commit credentials to GitHub
* ✅ Password is requested **only when needed**

---

## 🎯 Ideal Use Cases

* Local system health checks
* Lightweight monitoring for personal servers
* Learning system monitoring concepts
* Small DevOps / SRE practice projects

---

## 🧩 Limitations 

* ❌ Not a replacement for Prometheus/Grafana
* ❌ No background daemon mode
* ❌ Email-only alerts (no Slack/Webhooks yet)

This is **intentionally simple**.

---

## 📌 Future Improvements 

* Slack / Discord / Webhook alerts
* Config file instead of hardcoded thresholds
* Background service mode
* Log file support

---

## 👤 Author

**Preetam Kumar Badatya**
Built for clarity, learning, and practical system monitoring.

---

⭐ If this helped you understand system health monitoring better — star the repo.

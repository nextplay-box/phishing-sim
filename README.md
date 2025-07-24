# 🎯 Phishing Simulation Project

A simple Python-based phishing simulation that mimics a fake Facebook login page to demonstrate how credential harvesting works **for ethical and educational purposes only**.

> 🔒 This project is intended strictly for cybersecurity awareness, ethical hacking education, or penetration testing within legally authorized environments. Do not use for malicious purposes.

---

## 🛠️ How It Works

- Hosts a local server on `http://localhost:8080`
- Displays a fake login form (e.g., `fake_facebook.html`)
- Captures and logs POSTed data into `logs/captured_data.txt`
- Useful for learning how phishing attacks work and how to defend against them

---

## 🚀 Getting Started

### 1. Clone the repo or move into your folder
```bash
cd ~/phishing-sim

2. Run the server

python3 phishing_server.py


3. Open the site on your browser (inside the VM)

http://localhost:8080

💡 Works inside Parrot OS browser (Firefox). You may not access it from your host machine unless you tweak firewall/bridge settings.

---

📂 Project Structure

phishing-sim/
├── phishing_server.py
├── fake_facebook.html
├── logs/
│   └── captured_data.txt
├── screenshots/
│   ├── fake_facebook_page.png
│   ├── phishing_terminal.png
│   └── captured_data.png
└── README.md

---


📋 Sample Code Snippet

with open(LOG_FILE, "a") as f:
    f.write(post_data + "\n\n")

Captured POST data is written to logs/captured_data.txt.

🖼️ Screenshots

## 🖼️ Screenshots

### 📌 Tool Running in Terminal
![Server Start](screenshot/s1.png)

### 📌 Browser Phishing Page
![Phishing Page](screenshot/s2.png)

### 📌 Credentials Captured
![Logs](screenshot/s3.png)

### 📌 Sample Log File
![Log File](screenshot/s4.png)

### 📌 Folder Structure
![Project Structure](screenshot/s5.png)




🧠 Disclaimer
This tool is built only for ethical testing and awareness. Do not deploy against users or systems you do not have permission to test. Unauthorized use may violate laws and terms of service.

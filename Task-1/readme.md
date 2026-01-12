# Task 1: Basic Network Sniffer

## 📌 Objective
The objective of this task is to build a basic network sniffer using Python on Linux that captures and analyzes network traffic packets. The program helps in understanding how data flows through a network and how different protocols operate.

---

## 🛠 Tools & Technologies Used
- Operating System: Kali Linux
- Programming Language: Python 3
- Library: Scapy
- Privileges: Root (sudo)

---

## 📂 Files Included
- sniffer.py – Python script for capturing and analyzing packets
- README.md – Documentation for Task 1

---

## ⚙️ Features
- Captures live network packets
- Displays source and destination IP addresses
- Filters packets by protocol (TCP / UDP)
- Allows specifying number of packets to capture
- Option to save captured packet data

---

## ▶️ Commands to Run the Sniffer

### 1️⃣ Capture 5 TCP packets
```bash
sudo python3 sniffer.py --protocol tcp --count 5

2️⃣ Capture 100 UDP packets

sudo python3 sniffer.py --protocol udp --count 100

3️⃣ Capture packets and save output

sudo python3 sniffer.py --protocol tcp --count 20 --save output.txt

4️⃣ Capture packets without protocol filter

sudo python3 sniffer.py --count 10

🔐 Why sudo is Required

Packet sniffing uses raw sockets, which require elevated privileges on Linux systems. Therefore, the program must be executed using sudo.
📊 Sample Output

Source IP      : 10.56.128.144
Destination IP : 255.255.255.255
Protocol       : UDP
Source Port    : 6537
Destination Port: 6537
Payload        : b'13:1768196250921:BeyondTV:TV:1:BeyondTV:11171010001002101110011:0:34&#05851&#05880&#058df&#058d5&#05818\x00\x00'
------------------------------------------------------------

🧠 Learning Outcomes

    Understanding of network packet structure

    Practical knowledge of TCP and UDP protocols

    Experience with packet sniffing and traffic analysis

    Hands-on usage of Scapy in Linux

⚠️ Disclaimer

This tool is created strictly for educational purposes. Unauthorized packet sniffing on networks without permission is illegal and unethical.
✅ Conclusion

This task successfully demonstrates the implementation of a basic network sniffer using Python and Scapy on Kali Linux. The program captures real-time network traffic and analyzes key packet attributes, providing a strong foundation in network security concepts.

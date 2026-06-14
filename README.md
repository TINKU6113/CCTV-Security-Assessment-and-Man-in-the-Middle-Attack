# 📹 CCTV Security Assessment & Man-in-the-Middle Analysis

---

## 📌 Overview

This project demonstrates an **offensive security assessment of IP-based CCTV systems** in a controlled lab environment.

It focuses on identifying exposed camera infrastructure, analyzing insecure services, and demonstrating how attackers can exploit weak network and web configurations through reconnaissance and controlled Man-in-the-Middle (MITM) simulation.

The goal is to understand real-world IoT surveillance security risks and improve defensive awareness.

---

## 🧠 System Workflow
Network Reconnaissance
↓
CCTV Device Discovery
↓
Subnet & Service Enumeration
↓
Web Interface Analysis
↓
Protocol Exploitation Testing (HTTP / RTSP / RTMP / Telnet)
↓
MITM Simulation (ARP Spoofing)
↓
Traffic Analysis & Credential Exposure Assessment

---

## 🚀 Key Features

### 🔍 Network Reconnaissance
- Performed subnet scanning to identify CCTV devices
- Discovered exposed IP cameras and services
- Mapped network topology for attack surface analysis

---

### 📡 Service Enumeration & Analysis
- Identified exposed services:
  - HTTP (Web admin panels)
  - RTSP (video streaming)
  - RTMP (media streams)
  - Telnet (insecure remote access)
- Assessed authentication and configuration weaknesses

---

### 🕷️ Web & Interface Analysis
- Used Python-based web scraping and spidering techniques
- Extracted camera web interface endpoints
- Cloned login pages for security testing in controlled environment
- Analyzed weak authentication mechanisms

---

### 🧪 Exploitation Testing (Controlled Lab)
- Tested potential misconfigurations in:
  - HTTP login panels
  - RTSP stream access
  - Telnet services
- Evaluated exposure of sensitive camera feeds and metadata

---

### ⚡ Man-in-the-Middle (MITM) Simulation
- Performed **ARP spoofing-based MITM testing**
- Intercepted network traffic between camera and client
- Analyzed:
  - Credential exposure risks
  - Unencrypted data transmission
  - Session hijacking possibilities (simulated)

---

## 🖥️ Tools & Technologies

- Python (Automation & Web Spidering)
- Nmap (Network Scanning)
- Wireshark (Packet Analysis)
- Bettercap / ARP spoofing tools
- Linux (Attack simulation environment)
- Web scraping scripts (custom Python modules)

---

## 🧠 Skills Demonstrated

- Network Security & Reconnaissance
- IoT Security Analysis (CCTV Systems)
- Web Application Security Testing
- Man-in-the-Middle Attack Simulation
- Traffic Analysis & Packet Inspection
- Vulnerability Assessment of Embedded Devices
- Offensive Security Methodology

---

## ⚠️ Disclaimer

This project was conducted strictly in a **controlled lab environment** for educational and cybersecurity research purposes only.

It does not target or interact with any unauthorized real-world systems.

---

## 📦 Installation (if applicable)

```bash
pip install -r requirements.txt

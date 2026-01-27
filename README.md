# Python Port Scanner

## 🔐 Project Overview
This project is a Python-based TCP port scanner designed to help understand how network services operate and how open ports can affect system security. The tool simulates how security professionals and penetration testers identify exposed services on a target machine.

## 🎯 Purpose
The main purpose of this project is to:
- Learn how computers communicate over a network using TCP sockets
- Understand how attackers and defenders discover open services
- Build foundational skills for cybersecurity, network auditing, and system security

This project is intended for **educational and ethical security testing only**.

## ⚙️ How It Works
The scanner creates a TCP socket and attempts to establish a connection with a specified port on a target IP address.

- If the connection is successful, the port is marked as **OPEN**
- If the connection fails or times out, the port is marked as **CLOSED**

This behavior mimics the basic technique used by professional network scanning tools.

## 🚀 Features
- Scan a single TCP port on any target IP
- Fast response using configurable timeout
- Clear open/closed status output
- Lightweight and beginner-friendly design

## 🛠️ Technologies Used
- Python 3
- Socket Programming (TCP/IP Networking)

## 📌 Usage
1. Run the program:
   ```bash
   python scanner.py
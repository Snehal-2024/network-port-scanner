# Network Port Scanner

This is a Python-based network port scanner that detects open ports on a target system.

## Features
- Scans ports from 1 to 1024
- Detects open TCP ports
- Identifies common services (HTTP, HTTPS, SSH, etc.)
- Uses multithreading for faster scanning

## Technologies Used
- Python
- Socket Programming
- Networking Concepts

## How It Works
The scanner attempts to connect to each port on the target system. 
If the connection is successful, the port is marked as open.

## Example
Target: google.com  
Open Ports: 80 (HTTP), 443 (HTTPS)

## Purpose
This project helps understand network communication, port behavior, and basic cybersecurity concepts.

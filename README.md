# CodeAlpha Basic Network Sniffer

## Overview
This project is a basic network sniffer built with Python and Scapy. It captures and analyzes IP packets on a network interface.

## Features
- Captures network packets.
- Displays source and destination IP addresses.
- Identifies TCP, UDP, ICMP, and other IP traffic.
- Displays source and destination ports when applicable.
- Shows packet size, timestamp, and packet number.
- Handles common packet-capture errors.

## Requirements
- Python 3
- Scapy
- Kali Linux or another compatible Linux system

## Installation
Install Scapy on Kali Linux:

```bash
sudo apt install python3-scapy
```

## Usage
Run the program with administrator privileges:

```bash
sudo python3 sniffer.py
```

The program captures up to 20 packets on the `eth0` interface.

## Learning Outcome
This project demonstrates basic packet capture, network protocol identification, and analysis of packet headers.

## Ethical Use
Only capture traffic on systems and networks you own or have explicit permission to inspect. This tool displays packet metadata and does not intentionally print packet payloads.

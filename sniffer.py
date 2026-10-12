from datetime import datetime
from scapy.all import sniff, IP, TCP, UDP, ICMP

packet_count = 0

def analyze_packet(packet):
    global packet_count

    if IP not in packet:
        return

    packet_count += 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    packet_size = len(packet)

    if TCP in packet:
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport
    elif UDP in packet:
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport
    elif ICMP in packet:
        protocol = "ICMP"
        source_port = "-"
        destination_port = "-"
    else:
        protocol = "Other IP"
        source_port = "-"
        destination_port = "-"

    print(f"Packet #{packet_count} | {timestamp}")
    print(f"Source: {source_ip}:{source_port}")
    print(f"Destination: {destination_ip}:{destination_port}")
    print(f"Protocol: {protocol}")
    print(f"Packet size: {packet_size} bytes")
    print("-" * 40)


print("CodeAlpha Basic Network Sniffer")
print("Interface: eth0")
print("Capturing 20 packets...")

try:
    sniff(iface="eth0", prn=analyze_packet, count=20, store=False)
except KeyboardInterrupt:
    print("\nCapture stopped by user.")
except PermissionError:
    print("Permission denied. Run with sudo.")
except OSError as error:
    print(f"Capture error: {error}")

print("Capture finished.")

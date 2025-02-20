from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_handler(packet):
    print("\n📦 Captured a Packet!")

    # Display basic info
    if IP in packet:
        print(f"🌐 Source: {packet[IP].src} -> Destination: {packet[IP].dst}")

    if TCP in packet:
        print(f"🔵 TCP Packet | Source Port: {packet[TCP].sport} -> Destination Port: {packet[TCP].dport}")

    elif UDP in packet:
        print(f"🟠 UDP Packet | Source Port: {packet[UDP].sport} -> Destination Port: {packet[UDP].dport}")

    # Extract and display raw packet data (payload)
    if packet.haslayer(Raw):
        try:
            payload = packet[Raw].load.decode('utf-8', errors='ignore')
            if "HTTP" in payload:
                print(f"📜 HTTP Data:\n{payload}")
        except Exception as e:
            print(f"❌ Could not decode payload: {e}")

    print("-" * 50)  # Separator for readability

# Start sniffing (adjust iface as needed)
print("🚀 Sniffing started... Press Ctrl+C to stop.")
sniff(prn=packet_handler, filter="tcp port 80 or udp port 53", store=False)

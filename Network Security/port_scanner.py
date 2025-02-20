import nmap

def nmap_scan(target, start_port, end_port):
    scanner = nmap.PortScanner("C:\\Program Files (x86)\\Nmap")
    print(f"🔍 Scanning {target} from port {start_port} to {end_port}...\n")

    # Run an nmap scan
    scanner.scan(target, f"{start_port}-{end_port}", arguments="-sV")  # -sV: Service detection

    for host in scanner.all_hosts():
        print(f"🎯 Target: {host}")
        for port in scanner[host]["tcp"]:
            state = scanner[host]["tcp"][port]["state"]
            service = scanner[host]["tcp"][port]["name"]
            print(f"✅ Port {port}: {state} ({service})")

    print("\n🎯 Scan complete!")

# User input for target and port range
target_host = input("Enter target IP or domain: ")
start_port = input("Enter start port: ")
end_port = input("Enter end port: ")

# Run the scan
nmap_scan(target_host, start_port, end_port)

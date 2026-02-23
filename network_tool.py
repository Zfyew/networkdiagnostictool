# Network Diagnostic Tool
# v5: single menu that loops so you can run multiple checks without restarting

import subprocess
import platform
import socket

def ping(host):
    print(f"\n[*] Pinging {host}...\n")
    flag = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(
        ["ping", flag, "4", host],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if result.returncode == 0:
        print(result.stdout)
        print("[+] Host is reachable.")
    else:
        print(result.stderr)
        print("[-] Host is unreachable.")

def dns_lookup(host):
    print(f"\n[*] Running DNS lookup for {host}...\n")
    try:
        ip = socket.gethostbyname(host)
        print(f"[+] {host} resolved to {ip}")
        try:
            reverse = socket.gethostbyaddr(ip)
            print(f"[+] Reverse lookup: {reverse[0]}")
        except socket.herror:
            print("[-] Reverse lookup failed.")
    except socket.gaierror:
        print(f"[-] Could not resolve {host}. Check the hostname.")

def traceroute(host):
    print(f"\n[*] Running traceroute to {host}...\n")
    command = ["tracert", host] if platform.system().lower() == "windows" else ["traceroute", host]
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(result.stderr)
        print("[-] Traceroute failed.")

def port_scan(host):
    print(f"\n[*] Scanning common ports on {host}...\n")
    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3389: "RDP"
    }
    try:
        ip = socket.gethostbyname(host)
        print(f"[*] Scanning {ip}...\n")
        for port, service in common_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"    [+] Port {port} ({service}) is OPEN")
            else:
                print(f"    [-] Port {port} ({service}) is closed")
            sock.close()
    except socket.gaierror:
        print(f"[-] Could not resolve {host}.")

def show_menu():
    print("\n==============================")
    print("   NETWORK DIAGNOSTIC TOOL   ")
    print("==============================")
    print("1. Ping")
    print("2. DNS Lookup")
    print("3. Traceroute")
    print("4. Port Scanner")
    print("5. Exit")
    print("==============================")

# keep running until user exits
while True:
    show_menu()
    choice = input("\nSelect option (1-5): ").strip()

    if choice == "5":
        print("\nExiting. Bye.\n")
        break

    if choice in ("1", "2", "3", "4"):
        host = input("Enter host (e.g. google.com): ").strip()
    
    if choice == "1":
        ping(host)
    elif choice == "2":
        dns_lookup(host)
    elif choice == "3":
        traceroute(host)
    elif choice == "4":
        port_scan(host)
    else:
        print("[-] Invalid option.")
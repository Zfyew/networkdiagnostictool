# Network Diagnostic Tool
# v6: cleaner output, better error handling throughout

import subprocess
import platform
import socket

# separator line to keep output readable between checks
DIVIDER = "\n" + "=" * 32

def ping(host):
    print(f"\n[*] Pinging {host}...\n")
    flag = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        result = subprocess.run(
            ["ping", flag, "4", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=15
        )
        if result.returncode == 0:
            print(result.stdout)
            print("[+] Host is reachable.")
        else:
            print("[-] Host is unreachable or did not respond.")
    except subprocess.TimeoutExpired:
        print("[-] Ping timed out.")
    except Exception as e:
        print(f"[-] Something went wrong: {e}")

def dns_lookup(host):
    print(f"\n[*] DNS lookup for {host}...\n")
    try:
        ip = socket.gethostbyname(host)
        print(f"[+] {host} -> {ip}")
        try:
            reverse = socket.gethostbyaddr(ip)
            print(f"[+] Reverse: {reverse[0]}")
        except socket.herror:
            print("[-] Reverse lookup failed.")
    except socket.gaierror:
        print(f"[-] Could not resolve {host}. Check the hostname.")

def traceroute(host):
    print(f"\n[*] Traceroute to {host}...\n")
    command = ["tracert", host] if platform.system().lower() == "windows" else ["traceroute", host]
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60
        )
        if result.returncode == 0:
            print(result.stdout)
        else:
            print("[-] Traceroute failed.")
    except subprocess.TimeoutExpired:
        print("[-] Traceroute timed out.")
    except Exception as e:
        print(f"[-] Something went wrong: {e}")

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
        print(f"[*] Target: {ip}\n")
        for port, service in common_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            status = "OPEN" if result == 0 else "closed"
            tag = "[+]" if result == 0 else "[-]"
            print(f"    {tag} {port:<6} {service:<10} {status}")
            sock.close()
    except socket.gaierror:
        print(f"[-] Could not resolve {host}.")
    except Exception as e:
        print(f"[-] Something went wrong: {e}")

def show_menu():
    print(DIVIDER)
    print("     NETWORK DIAGNOSTIC TOOL")
    print(DIVIDER)
    print("  1. Ping")
    print("  2. DNS Lookup")
    print("  3. Traceroute")
    print("  4. Port Scanner")
    print("  5. Exit")
    print(DIVIDER)

while True:
    show_menu()
    choice = input("\nSelect option (1-5): ").strip()

    if choice == "5":
        print("\nDone.\n")
        break

    if choice in ("1", "2", "3", "4"):
        host = input("Enter host (e.g. google.com): ").strip()
        if not host:
            print("[-] No host entered.")
            continue

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
# Network Diagnostic Tool
# v3: added traceroute

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

print("\n==============================")
print("   NETWORK DIAGNOSTIC TOOL   ")
print("==============================")
print("1. Ping")
print("2. DNS Lookup")
print("3. Traceroute")
print("==============================")

choice = input("\nSelect option (1-3): ")
host = input("Enter host (e.g. google.com): ")

if choice == "1":
    ping(host)
elif choice == "2":
    dns_lookup(host)
elif choice == "3":
    traceroute(host)
else:
    print("[-] Invalid option.")
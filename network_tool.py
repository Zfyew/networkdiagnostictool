# Network Diagnostic Tool
# v2: added DNS lookup

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

print("\n==============================")
print("   NETWORK DIAGNOSTIC TOOL   ")
print("==============================")
print("1. Ping")
print("2. DNS Lookup")
print("==============================")

choice = input("\nSelect option (1-2): ")
host = input("Enter host (e.g. google.com): ")

if choice == "1":
    ping(host)
elif choice == "2":
    dns_lookup(host)
else:
    print("[-] Invalid option.")
# Network Diagnostic Tool
# v1: ping function

import subprocess
import platform

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

host = input("Enter host to ping (e.g. google.com): ")
ping(host)
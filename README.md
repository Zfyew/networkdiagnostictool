# Network Diagnostic Tool

Python script for running basic network checks from one place rather than 
jumping between different tools and commands.

## How to run

    python network_tool.py

Pick an option from the menu and enter a host like google.com.

## What it does

- Ping a host to check if its reachable
- DNS lookup to see what IP a hostname resolves to, with reverse lookup
- Traceroute to see the path packets take to get to a host
- Port scan across common ports to see whats open

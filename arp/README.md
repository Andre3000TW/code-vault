# ARP
Send out an ARP frame to get the target host MAC address. (Must be in the same LAN)

# Usage
1. Modify interface name in [arp.py line #7](https://github.com/Andre3000TW/code-vault/blob/5eef06cc5dfcd9a77af179549f10651044dec410/arp/source/arp.py#L7)
2. Modify sender IP address in [arp.py line #25](https://github.com/Andre3000TW/code-vault/blob/5eef06cc5dfcd9a77af179549f10651044dec410/arp/source/arp.py#L25)
3. Modify target IP address in [arp.py line #27](https://github.com/Andre3000TW/code-vault/blob/5eef06cc5dfcd9a77af179549f10651044dec410/arp/source/arp.py#L27)
4. Run it and you should get the target host MAC address

# Test Environment
+ Kali Linux 2020.1 64-bit
+ Python 3.9.0

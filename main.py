import socket
from subdomains import sub_domains
import os

user = input("Enter domain name(e.g. google.com): ")

found = []

for s in sub_domains:
    domain = f"{s}.{user}"
    try:
        ip = socket.gethostbyname(domain)
        print(f"=============================")
        print(f"[+] FOUND: {domain} → {ip}")
        found.append((domain, ip))
        print(f"=============================")
    except:
        pass


if found:
    saving = input("Do you want to save the results ? (yes/no)")
    if saving.lower() == "yes":
        pick_a_name = input("Enter the file name you want to save the results: ")

        with open(pick_a_name, mode="w", encoding="utf-8") as file:
            file.write(f"Subdomain scan results for {user}\n")
            file.write("="*50 + "\n\n")
            for domain, ip in found:
                file.write(f"{domain} --> {ip} \n")
            file.write(f"Total findings: {len(found)} \n")
        print(f"Results saved in {pick_a_name}")
    else:
        print("No results saved")
else:
    print("No subdomains found to save")

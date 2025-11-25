import socket
import argparse
from subdomains import sub_domains
import os
def main():
    parser = argparse.ArgumentParser(description='Subdomain Scanner')
    parser.add_argument('-d', '--domain', required=True, help='Domain to scan (e.g. google.com)')
    parser.add_argument('-o', '--output', help='Output file name')
    args = parser.parse_args()

    found = []

    for s in sub_domains:
        domain = f"{s}.{args.domain}"
        try:
            ip = socket.gethostbyname(domain)
            print(f"=============================")
            print(f"[+] FOUND: {domain} → {ip}")
            found.append((domain, ip))
            print(f"=============================")
        except:
            pass


    if found:
        if args.output:
            with open(args.output, mode="w", encoding="utf-8") as file:
                file.write(f"Subdomain scan results for {args.domain}\n")
                file.write("="*50 + "\n\n")
                for domain, ip in found:
                    file.write(f"{domain} --> {ip} \n")
                file.write(f"Total findings: {len(found)} \n")
            print(f"Results saved in {args.output}")
        else:
            print("No results saved")
    else:
        print("No subdomains found to save")

if __name__ == "__main__":
    main()

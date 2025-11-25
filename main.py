import socket
import argparse
from subdomains import sub_domains
from datetime import datetime
import os
def main():
    parser = argparse.ArgumentParser(description='Subdomain Scanner',
                                     epilog='python main.py -d example.com'
                                            'python main.py -d target.org -o results.txt')
    parser.add_argument('-d', '--domain', required=True, help='Domain to scan (e.g. google.com)')
    parser.add_argument('-o', '--output', help='Output file name')
    args = parser.parse_args()

    print(f'Running subdomain scan on {args.domain}..........')

    found = []

    for sub in sub_domains:
        target = f"{sub}.{args.domain}"
        try:
            ip = socket.gethostbyname(target)
            print(f"=============================")
            print(f"[+] FOUND: {target} → {ip}")
            found.append((target, ip))
            print(f"=============================")
        except socket.gaierror:
            print("No DNS records")
            pass

    if found:
        if args.output:
            with open(args.output, mode="w", encoding="utf-8") as report:
                report.write(f"Subdomain scan results for {args.domain}\n")
                date_of_the_scan = datetime.now().strftime("%d/%m/%Y %S:%M:%H")
                report.write(f"Scan done in {date_of_the_scan}\n")
                report.write("="*50 + "\n\n")
                report.write(f"Available subdomains checked {len(found)}\n")

                for domain, ip in found:
                    report.write(f"{domain} --> {ip} \n")
            print(f"Results saved in {args.output}")
        else:
            print("[*] No output file specified. Use -o to save results.")
    else:
        print("No subdomains found to save")

if __name__ == "__main__":
    main()

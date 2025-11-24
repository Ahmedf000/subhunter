import socket
import os

user = input("Enter domain name: ")
subdomains = [
    "www",
    "mail",
    "dev",
    "api",
    "test",
    "staging",
    "stage",
    "beta",
    "admin",
    "portal",
    "dashboard",
    "secure",
    "vpn",
    "cpanel",
    "webmail",
    "support",
    "help",
    "shop",
    "store",
    "blog",
    "static",
    "cdn",
    "img",
    "files",
    "assets",
    "app",
    "login",
    "sso",
    "internal",
    "server"
]


for s in subdomains:
    domain = f"{s}.{user}.com"
    try:
        ip = socket.gethostbyname(domain)
        print(f"=============================")
        print(f"[+] Trying to connect to {ip}")
        print(f"Connected to {domain}")
        print(f"=============================")
    except:
        print(f"couldn't connect to {domain}")

saving = input("Do you want to save the results ? (yes/no)")
if saving.lower() == "no":
    print("Goodbye")
    exit()
else:
    try:
        file_name = input("Enter file name: ")
        with open(file_name, mode="w", encoding="utf-8") as file:


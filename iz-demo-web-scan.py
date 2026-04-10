import os
import sys
import time
import random

# Paleta de colores - Estilo Cyber-Matrix (Parrot OS)
R = "\033[1;31m" 
G = "\033[1;32m" 
B = "\033[1;34m" 
Y = "\033[1;33m" 
W = "\033[1;37m" 
C = "\033[1;36m" 
P = "\033[1;35m" 
reset = "\033[0m"

def banner():
    os.system("clear")
    print(f"{P}")
    print(r"""
  ██ ███████        ██     ██ ███████ ██████        ███████  ██████  █████  ███    ██ 
  ██      ██        ██     ██ ██      ██   ██       ██      ██    ██ ██   ██ ████   ██ 
  ██   ████         ██  █  ██ █████   ██████        ███████ ██    ██ ███████ ██ ██  ██ 
  ██  ██            ██ ███ ██ ██      ██   ██            ██ ██    ██ ██   ██ ██  ██ ██ 
  ██ ███████         ███ ███  ███████ ██████        ███████  ██████ ██   ██ ██   ████ 
    """)
    print(f"{W}      -- [ DEMO MULTI-SCANNER SUITE ] -- [ v1.0 BY IZ4CXZ_BY ] --{reset}")
    print(f"{C}      [ DATABASE: LIMITED | ENCRYPTION: AES-256 | NODES: ACTIVE ]{reset}\n")

# --- FUNCIONES RECORTADAS PARA LA DEMO ---

def username_tracker():
    banner()
    user = input(f"{Y} Enter Username: {reset}")
    print(f"\n{C}[*] Scanning 20 Basic Platforms for '{user}'...{reset}\n")
    
    # Recortado a los 20 más comunes
    platforms = [
        "Instagram", "Facebook", "Twitter", "TikTok", "GitHub", "YouTube", "Reddit", "Snapchat",
        "LinkedIn", "Pinterest", "Telegram", "Twitch", "Discord", "Steam", "Spotify", "Roblox",
        "Medium", "Tumblr", "Behance", "Dribbble"
    ]
    
    found_count = 0
    for site in platforms:
        # Lógica de demo: menos probabilidad de "FOUND"
        status = random.choice([f"{G}[+] FOUND", f"{R}[-] NOT FOUND", f"{R}[-] NOT FOUND", f"{R}[-] NOT FOUND"])
        if "FOUND" in status:
            found_count += 1
        print(f"{W}[*] Searching {site:15} {status}{reset}")
        time.sleep(0.1) 
        
    print(f"\n{C}--------------------------------------------------{reset}")
    print(f"{G}[!] Scan Finished. Total Accounts Found: {found_count}{reset}")
    print(f"{Y}[i] Full scan (50+ sites) available in PREMIUM version.{reset}")
    print(f"{C}--------------------------------------------------{reset}")
    input(f"\n{P}Press Enter to return to menu...{reset}")

def email_breach():
    banner()
    email = input(f"{Y} Enter Email: {reset}")
    print(f"\n{C}[*] Querying Limited Leak Archives...{reset}")
    time.sleep(2)
    # Solo muestra una filtración básica para que se queden con ganas de más
    print(f"\n{R}[ALERT] PARTIAL BREACH DETECTED:{reset}")
    print(f"{W}- Common Data Leak (Source Masked){reset}")
    print(f"\n{Y}[i] Full breach details and source list are PREMIUM-only.{reset}")
    input(f"\n{P}Press Enter to return...{reset}")

def domain_investigator():
    banner()
    domain = input(f"{Y} Enter Domain: {reset}")
    print(f"\n{C}[*] Extracting Basic DNS Info...{reset}")
    time.sleep(1.5)
    print(f"{G}[+] Target IP:   {W}104.21.{random.randint(10,99)}.{random.randint(100,255)}{reset}")
    print(f"{G}[+] Provider:    {W}Cloudflare, Inc.{reset}")
    print(f"\n{Y}[i] Deep WHOIS and Infrastructure mapping is LOCKED.{reset}")
    input(f"\n{P}Press Enter to return...{reset}")

def module_locked():

    print(f"\n{R}[!] ACCESS DENIED{reset}")

    print(f"{W}This module is {G}LOCKED{W} in the DEMO version.{reset}")

    print(f"{Y}To get the PREMIUM version, support the project here:{reset}")

    print(f"{C}👉 https://ko-fi.com/iz4cxz_by{reset}")

    print(f"{W}After payment, contact me for your license key.{reset}")

    time.sleep(3)
# --- BUCLE PRINCIPAL ---

def main():
    while True:
        banner()
        # Mantenemos las etiquetas originales para que se vea potente
        print(f"{C}   --- OSINT MODULES (AVAILABLE) ---")
        print(f"{P}[01]{W} Username Tracker       {G}(Social-Media Forensic){reset}")
        print(f"{P}[02]{W} Email Breach Checker   {G}(Deep Web Leak Scan){reset}")
        print(f"{P}[03]{W} Domain/IP Investigator {G}(Infrastructure Recon){reset}")
        
        print(f"\n{R}   --- ADVANCED WEB MODULES (PRO) ---")
        print(f"{P}[04]{W} CMS & Tech Detector    {R}[LOCKED]{reset}")
        print(f"{P}[05]{W} Subdomain Finder       {R}[LOCKED]{reset}")
        print(f"{P}[06]{W} Social Engineering Tool{R}[LOCKED]{reset}")
        print(f"{P}[07]{W} Cloudflare Resolver    {R}[LOCKED]{reset}")
        print(f"{P}[08]{W} Web Port Scanner       {R}[LOCKED]{reset}")
        
        print(f"\n{R}[00]{W} EXIT SYSTEM")
        
        choice = input(f"\n{P}IZ-DEMO-SCAN >> {reset}")
        
        if choice in ["1", "01"]: username_tracker()
        elif choice in ["2", "02"]: email_breach()
        elif choice in ["3", "03"]: domain_investigator()
        elif choice in ["4", "04", "5", "05", "6", "06", "7", "07", "8", "08"]: module_locked()
        elif choice == "00":
            print(f"{R}\n[!] System Offline.{reset}")
            sys.exit()
        else:
            print(f"{R}[!] Invalid Option.{reset}"); time.sleep(1)

if __name__ == "__main__":
    main()

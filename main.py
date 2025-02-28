import os
import sys
import time
import requests
import json
from datetime import datetime
from colorama import Fore, Style
import itertools
import threading

# **स्क्रीन क्लियर करें**  
os.system('clear')

# **लोगो एनिमेशन**  
def logo_animation():
    logo = """
\033[1;36m  
██████╗  ██████╗  ██████╗ ██╗  ██╗███████╗███╗   ██╗
██╔══██╗██╔═══██╗██╔════╝ ██║  ██║██╔════╝████╗  ██║
██████╔╝██║   ██║██║  ███╗███████║█████╗  ██╔██╗ ██║
██╔═══╝ ██║   ██║██║   ██║██╔══██║██╔══╝  ██║╚██╗██║
██║     ╚██████╔╝╚██████╔╝██║  ██║███████╗██║ ╚████║
╚═╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
\033[0m
"""
    for char in logo:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.002)

logo_animation()

# **लोडिंग एनिमेशन**  
def loading_animation(text, duration=3):
    spinner = itertools.cycle(["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(f"\r{Fore.YELLOW}{text} {next(spinner)}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.1)
    print("")

# **इंटरनेट चेक फंक्शन**  
def check_internet():
    while True:
        try:
            requests.get("https://www.google.com", timeout=5)
            return True
        except requests.ConnectionError:
            print(Fore.RED + "❌ इंटरनेट नहीं मिला, 5 सेकंड में पुनः प्रयास..." + Style.RESET_ALL)
            time.sleep(5)

# **पासवर्ड वेरिफिकेशन**  
def password_auth():
    correct_password = "12345"  # **अपना पासवर्ड सेट करें**
    while True:
        password = input(Fore.GREEN + "🔒 पासवर्ड दर्ज करें: " + Style.RESET_ALL)
        if password == correct_password:
            loading_animation("पासवर्ड सत्यापित किया जा रहा है", 2)
            print(Fore.YELLOW + "✅ लॉगिन सफल!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "❌ गलत पासवर्ड! दोबारा कोशिश करें।" + Style.RESET_ALL)

# **एक्सेस टोकन फाइल लोड करें**  
def load_tokens():
    while True:
        token_file = input(Fore.CYAN + "📂 टोकन फाइल का नाम दर्ज करें: " + Style.RESET_ALL)
        if os.path.exists(token_file):
            with open(token_file, 'r') as f:
                tokens = f.read().splitlines()
            return tokens
        else:
            print(Fore.RED + "❌ फाइल नहीं मिली! सही नाम दर्ज करें।" + Style.RESET_ALL)

# **Facebook Profile Name निकालें**  
def get_profile_name(access_token):
    try:
        url = f'https://graph.facebook.com/me?access_token={access_token}'
        response = requests.get(url)
        data = response.json()
        if 'name' in data:
            return data['name']
        return None
    except:
        return None

# **मैसेज भेजने का फंक्शन**  
def send_message(access_token, user_id, message):
    url = f"https://graph.facebook.com/{user_id}/comments"
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {'message': message}

    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        print(Fore.GREEN + f"[✔] {user_id} को मैसेज भेजा गया: {message}" + Style.RESET_ALL)
        return True
    else:
        print(Fore.RED + f"[✖] {user_id} को मैसेज भेजने में विफल!" + Style.RESET_ALL)
        return False

# **प्रगति बार**  
def progress_bar(total, prefix="प्रगति"):
    for i in range(total + 1):
        percent = (i / total) * 100
        bar = "█" * i + "-" * (total - i)
        sys.stdout.write(f"\r{Fore.CYAN}{prefix}: |{bar}| {percent:.2f}%{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.05)
    print("")

# **मेन प्रोसेस**  
def main():
    check_internet()
    password_auth()
    access_tokens = load_tokens()

    # **प्रोफाइल जानकारी निकालें**  
    for token in access_tokens:
        profile_name = get_profile_name(token)
        if profile_name:
            print(Fore.YELLOW + f"✅ लॉग इन: {profile_name}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "❌ गलत या एक्सपायर टोकन!" + Style.RESET_ALL)
            continue

    user_id = input(Fore.CYAN + "🎯 टारगेट पोस्ट आईडी दर्ज करें: " + Style.RESET_ALL)
    message = input(Fore.GREEN + "💬 भेजने के लिए मैसेज दर्ज करें: " + Style.RESET_ALL)

    confirm = input(Fore.YELLOW + "⚠️ क्या आप मैसेज भेजना चाहते हैं? (yes/no): " + Style.RESET_ALL).lower()
    if confirm != "yes":
        print(Fore.RED + "❌ ऑपरेशन कैंसिल कर दिया गया।" + Style.RESET_ALL)
        return

    delay_time = int(input(Fore.CYAN + "⏳ प्रत्येक मैसेज के बीच डिले (सेकंड में): " + Style.RESET_ALL))

    print(Fore.MAGENTA + "\n🚀 मैसेज भेजना शुरू हो रहा है..." + Style.RESET_ALL)
    progress_bar(20, "संदेश प्रसंस्करण")

    for token in access_tokens:
        send_message(token, user_id, message)
        time.sleep(delay_time)

    print(Fore.GREEN + "🎉 सभी मैसेज सफलतापूर्वक भेज दिए गए!" + Style.RESET_ALL)

# **स्क्रिप्ट चलाएं**  
if __name__ == "__main__":
    main()

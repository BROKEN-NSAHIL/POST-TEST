import random
import string
import os
import time

# 🌟 टर्मिनल क्लियर करने का फंक्शन
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# 🎨 कस्टम लोगो
def show_logo():
    logo = """
    █████╗  ██████╗ ██████╗███╗   ███╗ █████╗ ██╗   ██╗████████╗
    ██╔══██╗██╔════╝██╔════╝████╗ ████║██╔══██╗██║   ██║╚══██╔══╝
    ███████║██║     ██║     ██╔████╔██║███████║██║   ██║   ██║   
    ██╔══██║██║     ██║     ██║╚██╔╝██║██╔══██║██║   ██║   ██║   
    ██║  ██║╚██████╗╚██████╗██║ ╚═╝ ██║██║  ██║╚██████╔╝   ██║   
    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   
    """
    print(logo)
    print("🔥 Auto Account Generator - OFFLINE Version 🔥")
    print("=================================================\n")

# 📨 रैंडम ईमेल जनरेटर
def random_email():
    domains = ["@edny.net", "@xyzmail.com", "@tempmail.net"]
    prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return prefix + random.choice(domains)

# 🔐 रैंडम पासवर्ड जनरेटर
def random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=10))

# 👤 रैंडम नाम जनरेटर
def random_name():
    first_names = ["Neil", "Kyle", "Ronald", "John", "Alice", "Emma"]
    last_names = ["Hall", "James", "Vazquez", "Smith", "Brown", "Davis"]
    return random.choice(first_names) + " " + random.choice(last_names)

# 📅 रैंडम बर्थडे जनरेटर
def random_birthday():
    year = random.randint(1980, 2010)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year}-{month:02d}-{day:02d}"

# 🚻 रैंडम जेंडर
def random_gender():
    return random.choice(["M", "F"])

# 🔑 रैंडम टोकन जेनरेट
def generate_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=100))

# 📂 डेटा को फाइल में सेव करने का फंक्शन
def save_to_file(data):
    with open("accounts.txt", "a") as file:
        file.write(data + "\n")

# 🆕 अकाउंट क्रिएट करने का फंक्शन
def create_account():
    email = random_email()
    user_id = random.randint(600000000000, 699999999999)
    password = random_password()
    name = random_name()
    birthday = random_birthday()
    gender = random_gender()
    token = generate_token()

    account_data = f"""
    -----------ACCOUNT-CREATED-----------
    EMAIL    : {email}
    ID       : {user_id}
    PASSWORD : {password}
    NAME     : {name}
    BIRTHDAY : {birthday}
    GENDER   : {gender}
    -----------TOKEN-----------
    {token}
    -------------------------------------
    """
    
    print(account_data)
    save_to_file(account_data)  # फाइल में सेव करें

# 🔥 मेन प्रोग्राम
def main():
    clear_screen()
    show_logo()
    
    try:
        num_accounts = int(input("[+] How Many Accounts You Want: "))
        print("\n🔄 Generating Accounts...\n")
        time.sleep(1)

        for _ in range(num_accounts):
            create_account()
            time.sleep(0.5)

        print("\n✅ All Accounts Generated Successfully!")
        print("📂 Saved in: accounts.txt\n")
    
    except ValueError:
        print("\n❌ Invalid Input! Please enter a number.")

# 🏁 रन प्रोग्राम
if __name__ == "__main__":
    main()

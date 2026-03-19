import os
import json

# ==============================
# 📁 FILE HANDLING FUNCTIONS (JSON)
# ==============================

def save_data(users, file='users.json'):
    """
    Saves user data into a JSON file.
    """
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


def load_data(file='users.json'):
    """
    Loads data from a JSON file.
    If the file does not exist, returns an empty dictionary.
    """
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


# ==============================
# 🖥️ UTILITIES
# ==============================

def clear_screen():
    """
    Clears the terminal screen (Windows / Linux / Mac).
    """
    os.system('cls' if os.name == 'nt' else 'clear')


# ==============================
# 👤 USER REGISTRATION
# ==============================

def register_user(users):
    """
    Registers a new user.
    Validates email and name before saving.
    """
    while True:
        email = input("Enter email: ").strip()

        # Simple email validation
        if '@' not in email:
            print("Invalid email.")
            continue

        if email in users:
            print("Email already registered.")
            return

        name = input("Name: ").strip()

        if not name:
            print("Name cannot be empty.")
            continue

        # Name must not contain numbers
        if any(char.isdigit() for char in name):
            print("Name cannot contain numbers.")
            continue

        users[email] = {
            'name': name,
            'transactions': []
        }

        print("\n✅ User registered successfully!")
        save_data(users)
        input("\nPress ENTER to continue...")
        return


# ==============================
# 💰 TRANSACTION REGISTRATION
# ==============================

def register_transaction(users, transaction_type):
    """
    Registers a transaction (income or expense).
    """
    email = input("Email: ").strip()

    if email not in users:
        print("Email not registered.")
        input("Press ENTER to continue...")
        return

    description = input("Description: ").strip()

    if not description:
        print("Description cannot be empty.")
        return

    try:
        value = float(input("Amount: $ "))

        if value <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Invalid value.")
        return

    transaction = {
        'type': transaction_type,
        'description': description,
        'value': value
    }

    users[email]['transactions'].append(transaction)
    save_data(users)

    print(f"\n✅ {transaction_type.capitalize()} registered successfully!")
    input("Press ENTER to continue...")


# ==============================
# 📋 LIST TRANSACTIONS
# ==============================

def list_transactions(users):
    """
    Displays all user transactions and calculates current balance.
    """
    email = input('Email: ').strip()

    if email not in users:
        print('Email not registered.')
        input("Press ENTER to continue...")
        return

    transactions = users[email]['transactions']

    if not transactions:
        print("No transactions found.")
        input("Press ENTER to continue...")
        return

    print("\n" + "=-" * 20)
    print(f"Transactions for {users[email]['name'].title()}")

    balance = 0

    for i, t in enumerate(transactions, start=1):
        print("=-" * 20)
        print(f"{i}. Type: {t['type']}")
        print(f"   Description: {t['description']}")
        print(f"   Amount: $ {t['value']:.2f}")

        if t['type'] == 'income':
            balance += t['value']
        else:
            balance -= t['value']

    print("=-" * 20)
    print(f"\n💰 Current balance: $ {balance:.2f}")
    input("\nPress ENTER to continue...")


# ==============================
# 📊 FINANCIAL REPORT
# ==============================

def financial_report(users):
    """
    Generates a financial summary:
    - Total income
    - Total expenses
    - Final balance
    """
    email = input('Email: ').strip()

    if email not in users:
        print('Email not registered.')
        input("Press ENTER to continue...")
        return

    total_income = 0
    total_expenses = 0

    for t in users[email]['transactions']:
        if t['type'] == 'income':
            total_income += t['value']
        elif t['type'] == 'expense':
            total_expenses += t['value']

    balance = total_income - total_expenses

    print(f"\n📊 Financial report for {users[email]['name'].title()}")
    print(f"Income: $ {total_income:.2f}")
    print(f"Expenses: $ {total_expenses:.2f}")
    print(f"Balance: $ {balance:.2f}")

    input("\nPress ENTER to continue...")


# ==============================
# 🚀 MAIN PROGRAM
# ==============================

users = load_data()

while True:
    clear_screen()

    print("=== FINANCIAL SYSTEM ===")
    print("[1] Register user")
    print("[2] Add income")
    print("[3] Add expense")
    print("[4] List transactions")
    print("[5] Financial report")
    print("[6] Exit")

    try:
        option = int(input("Choose an option: "))

        if option < 1 or option > 6:
            print("Invalid option.")
            input("Press ENTER to continue...")
            continue

    except ValueError:
        print("Enter a valid number.")
        input("Press ENTER to continue...")
        continue

    match option:
        case 1:
            register_user(users)
        case 2:
            register_transaction(users, 'income')
        case 3:
            register_transaction(users, 'expense')
        case 4:
            list_transactions(users)
        case 5:
            financial_report(users)
        case 6:
            print("Exiting system...")
            break
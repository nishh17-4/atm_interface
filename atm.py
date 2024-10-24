import hashlib

def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()

class ATM:
    def __init__(self):
        self.accounts = {}
        self.current_user = None

    def create_account(self, account_number, pin):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            hashed_pin = hash_pin(pin)
            self.accounts[account_number] = {'pin': hashed_pin, 'balance': 0, 'history': []}
            print(f"Account {account_number} created successfully.")

    def authenticate(self, account_number):
        if account_number in self.accounts:
            for i in range(3):  # Allow 3 attempts to enter PIN
                pin = input("Enter your PIN: ")  # Changed to input() to capture PIN
                hashed_pin = hash_pin(pin)
                if hashed_pin == self.accounts[account_number]['pin']:
                    self.current_user = account_number
                    print(f"Welcome, Account {account_number}!")
                    return True
                else:
                    print("Incorrect PIN. Try again.")
            print("Too many incorrect attempts. Try later.")
        else:
            print("Account does not exist.")
        return False

    # Remaining methods (deposit, withdraw, check balance, etc.) remain unchanged

def main():
    atm = ATM()

    while True:
        print("\n=== ATM Menu ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            # Keep asking for a valid 10-digit account number until the user enters it correctly
            while True:
                acc_num = input("Enter a new 10-digit account number: ")
                if len(acc_num) == 10 and acc_num.isdigit():
                    break
                print("Error: Account number must be exactly 10 digits.")

            # Keep asking for a valid 6-digit PIN until the user enters it correctly
            while True:
                pin = input("Create a 6-digit PIN: ")
                if len(pin) == 6 and pin.isdigit():
                    atm.create_account(acc_num, pin)  # Create account after valid PIN
                    break
                print("Error: PIN must be exactly 6 digits.")

        elif choice == '2':
            acc_num = input("Enter your 10-digit account number: ")
            if len(acc_num) == 10 and acc_num.isdigit():
                if atm.authenticate(acc_num):
                    while atm.current_user:
                        print("\n--- Logged In ---")
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Check Balance")
                        print("4. View Transaction History")
                        print("5. Logout")

                        user_choice = input("Choose an option: ")

                        if user_choice == '1':
                            amount = float(input("Enter amount to deposit: "))
                            atm.deposit(amount)
                        elif user_choice == '2':
                            amount = float(input("Enter amount to withdraw: "))
                            atm.withdraw(amount)
                        elif user_choice == '3':
                            atm.check_balance()
                        elif user_choice == '4':
                            atm.view_history()
                        elif user_choice == '5':
                            atm.logout()
                        else:
                            print("Invalid option.")
                else:
                    print("Authentication failed.")
            else:
                print("Invalid account number. It must be 10 digits.")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()

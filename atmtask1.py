import time
#******************* Simulate the ATM card insertion*****************#

print("Please insert your card")
time.sleep(2)

# ******************Initial account setup************************#

original_pin=1234
balance=5000
transaction_history=[]

# *****************Function to display the main menu*************#
def display_menu():
    print("""
    1 == Balance 
    2 == Withdraw Amount
    3 == Deposit Amount
    4 == PIN Change
    5 == Transaction History
    6 == Exit
    """)

# *****************Function to display transaction history****************#
def show_transaction_history():
    if not transaction_history:
        print("No transactions yet.")
    else:
        for transaction in transaction_history:
            print(transaction)

# *****************Main ATM functionality***************#
try:
    pin = int(input("Enter the ATM PIN: "))
except ValueError:
    print("Invalid PIN format. Please use only numbers.")
    exit()

if pin == original_pin:
    while True:
        display_menu()
        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option.")
            continue

        if option == 1:  # Balance Inquiry
            print(f"Your current balance is {balance}")
            transaction_history.append(f"Balance Inquiry: {balance}")
        
        elif option == 2:  # Cash Withdrawal
            try:
                withdraw_amount = int(input("Please enter withdrawal amount: "))
                if withdraw_amount <= balance:
                    balance -= withdraw_amount
                    print(f"{withdraw_amount} has been withdrawn from your account.")
                    print(f"Your updated balance is {balance}")
                    transaction_history.append(f"Withdrawal: {withdraw_amount}")
                else:
                    print("Insufficient balance.")
            except ValueError:
                print("Invalid amount format.")
        
        elif option == 3:  # Cash Deposit
            try:
                deposit_amount = int(input("Please enter deposit amount: "))
                balance += deposit_amount
                print(f"{deposit_amount} has been deposited into your account.")
                print(f"Your updated balance is {balance}")
                transaction_history.append(f"Deposit: {deposit_amount}")
            except ValueError:
                print("Invalid amount format.")
        
        elif option == 4:  # PIN Change
            try:
                new_pin = int(input("Enter your new PIN: "))
                confirm_pin = int(input("Confirm your new PIN: "))
                if new_pin == confirm_pin:
                    original_pin = new_pin
                    print("PIN changed successfully.")
                    transaction_history.append("PIN Change")
                else:
                    print("PINs do not match. Please try again.")
            except ValueError:
                print("Invalid PIN format. Please use only numbers.")
        
        elif option == 5:  # Transaction History
            show_transaction_history()
        
        elif option == 6:  # Exit
            print("Thank you for using our ATM.")
            break
        
        else:
            print("Invalid option. Please try again.")
else:
    print("Wrong PIN. Please try again.")

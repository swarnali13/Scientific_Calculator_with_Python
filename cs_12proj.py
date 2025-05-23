import mysql.connector

# Establish connection to the MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost", 
        user="root",       
        password="computer@13#", 
        database="atm_system"
    )

# Function to create a new account
def create_account():
    name = input("Enter your name: ")
    pin = int(input("Set a 4-digit PIN: "))
    
    db = connect_to_database()
    cursor = db.cursor()
    
    cursor.execute("INSERT INTO accounts (name, pin) VALUES (%s, %s)", (name, pin))
    db.commit()
    
    print("Account created successfully!")
    db.close()

# Function to check balance
def check_balance(account_number, pin):
    db = connect_to_database()
    cursor = db.cursor()
    
    cursor.execute("SELECT balance FROM accounts WHERE account_number = %s AND pin = %s", (account_number, pin))
    result = cursor.fetchone()
    
    if result:
        print(f"Your current balance is: ₹{result[0]}")
    else:
        print("Invalid account number or PIN.")
    db.close()

# Function to deposit money
def deposit(account_number, pin):
    amount = float(input("Enter amount to deposit: "))
    
    db = connect_to_database()
    cursor = db.cursor()
    
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_number = %s AND pin = %s", (amount, account_number, pin))
    db.commit()
    
    if cursor.rowcount > 0:
        print("Deposit successful!")
    else:
        print("Invalid account number or PIN.")
    db.close()

# Function to withdraw money
def withdraw(account_number, pin):
    amount = float(input("Enter amount to withdraw: "))
    
    db = connect_to_database()
    cursor = db.cursor()
    
    cursor.execute("SELECT balance FROM accounts WHERE account_number = %s AND pin = %s", (account_number, pin))
    result = cursor.fetchone()
    
    if result and result[0] >= amount:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_number = %s AND pin = %s", (amount, account_number, pin))
        db.commit()
        print("Withdrawal successful!")
    else:
        print("Insufficient balance or invalid credentials.")
    db.close()

# Function to change PIN
def change_pin(account_number, old_pin):
    new_pin = int(input("Enter new 4-digit PIN: "))
    
    db = connect_to_database()
    cursor = db.cursor()
    
    cursor.execute("UPDATE accounts SET pin = %s WHERE account_number = %s AND pin = %s", (new_pin, account_number, old_pin))
    db.commit()
    
    if cursor.rowcount > 0:
        print("PIN changed successfully!")
    else:
        print("Invalid account number or PIN.")
    db.close()

# Main menu
def main_menu():
    while True:
        print("\nATM Menu:")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Change PIN")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            create_account()
        elif choice in [2, 3, 4, 5]:
            account_number = int(input("Enter your account number: "))
            pin = int(input("Enter your PIN: "))
            
            if choice == 2:
                check_balance(account_number, pin)
            elif choice == 3:
                deposit(account_number, pin)
            elif choice == 4:
                withdraw(account_number, pin)
            elif choice == 5:
                change_pin(account_number, pin)
        elif choice == 6:
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()

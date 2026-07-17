# ATM Management System

class ATMSystem:
    def __init__(self, pin, initial_balance=0):
        """Initialize the ATM with a PIN and initial balance"""
        self.pin = pin
        self.balance = initial_balance
        self.transaction_history = []
    
    def verify_pin(self, entered_pin):
        """Verify if the entered PIN is correct"""
        return self.pin == entered_pin
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount <= 0:
            print("❌ Deposit amount must be positive!")
            return False
        
        self.balance += amount
        self.transaction_history.append(f"Deposited: ₹{amount}")
        print(f"✓ Successfully deposited ₹{amount}")
        return True
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
            return False
        
        if amount > self.balance:
            print(f"❌ Insufficient balance! Current balance: ₹{self.balance}")
            return False
        
        self.balance -= amount
        self.transaction_history.append(f"Withdrawn: ₹{amount}")
        print(f"✓ Successfully withdrawn ₹{amount}")
        return True
    
    def check_balance(self):
        """Display the current balance"""
        print(f"\n{'='*40}")
        print(f"Current Balance: ₹{self.balance}")
        print(f"{'='*40}\n")
        return self.balance
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*40)
        print("    ATM MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Exit")
        print("="*40)
    
    def show_transaction_history(self):
        """Display transaction history"""
        if not self.transaction_history:
            print("No transactions yet!")
            return
        
        print("\n--- Transaction History ---")
        for i, transaction in enumerate(self.transaction_history, 1):
            print(f"{i}. {transaction}")
        print()
    
    def run(self):
        """Main ATM operation loop"""
        print("\n" + "="*40)
        print("   WELCOME TO ATM SYSTEM")
        print("="*40)
        
        # PIN Verification
        attempts = 3
        while attempts > 0:
            entered_pin = input("\nEnter your PIN: ")
            
            if self.verify_pin(entered_pin):
                print("✓ PIN verified successfully!\n")
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"❌ Incorrect PIN! Attempts remaining: {attempts}")
                else:
                    print("❌ Maximum attempts exceeded. Account locked!")
                    return
        
        # Main Menu Loop
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                try:
                    amount = float(input("Enter amount to deposit: ₹"))
                    self.deposit(amount)
                except ValueError:
                    print("❌ Please enter a valid amount!")
            
            elif choice == '2':
                try:
                    amount = float(input("Enter amount to withdraw: ₹"))
                    self.withdraw(amount)
                except ValueError:
                    print("❌ Please enter a valid amount!")
            
            elif choice == '3':
                self.check_balance()
            
            elif choice == '4':
                self.show_transaction_history()
            
            elif choice == '5':
                print("\n" + "="*40)
                print("Thank you for using ATM System!")
                self.check_balance()
                print("="*40)
                break
            
            else:
                print("❌ Invalid choice! Please select 1-5.")


# Main Program
if __name__ == "__main__":
    # Create ATM instance with PIN: 1234 and initial balance: 5000
    atm = ATMSystem(pin="1234", initial_balance=5000)
    
    # Run the ATM system
    atm.run()

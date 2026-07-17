# ATM Management System

A comprehensive Python-based ATM system that simulates real-world banking operations with PIN authentication, deposits, withdrawals, and transaction tracking.

## Features

✅ **PIN Authentication** - Secure 3-attempt PIN verification  
✅ **Deposit Money** - Add funds to your account  
✅ **Withdraw Money** - With automatic balance verification  
✅ **Check Balance** - View your current account balance  
✅ **Transaction History** - Track all your transactions  
✅ **Input Validation** - Handles invalid inputs gracefully  
✅ **User-Friendly Interface** - Clear menus and status messages  

## System Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

```bash
git clone https://github.com/ankithkumarreddyk24cs-bit/ATM-Management-System.git
cd ATM-Management-System
```

## Usage

Run the ATM system:

```bash
python atm_system.py
```

### Default Credentials

- **PIN:** `1234`
- **Initial Balance:** ₹5000

### Menu Options

```
1. Deposit Money       - Add funds to your account
2. Withdraw Money      - Withdraw funds (with balance check)
3. Check Balance       - View current balance
4. View Transaction    - See all transactions
5. Exit                - Exit the system
```

## Program Flow

1. **Start Program** → User enters PIN
2. **PIN Verification** → Maximum 3 attempts allowed
3. **Main Menu** → Choose from 5 options
4. **Perform Transaction** → Deposit/Withdraw/Check Balance
5. **Transaction History** → View all past transactions
6. **Exit** → Display final balance and exit

## Example Session

```
===============================
   WELCOME TO ATM SYSTEM
===============================

Enter your PIN: 1234
✓ PIN verified successfully!

========================================
    ATM MANAGEMENT SYSTEM
========================================
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. View Transaction History
5. Exit
========================================
Enter your choice (1-5): 3

========================================
Current Balance: ₹5000
========================================

Enter your choice (1-5): 1
Enter amount to deposit: ₹2000
✓ Successfully deposited ₹2000

Enter your choice (1-5): 2
Enter amount to withdraw: ₹1500
✓ Successfully withdrawn ₹1500

Enter your choice (1-5): 3

========================================
Current Balance: ₹5500
========================================
```

## Security Features

- PIN protection with failed attempt limit
- Balance verification before withdrawal
- Transaction history tracking
- Input validation for all operations

## Error Handling

- Insufficient balance detection
- Invalid PIN attempts tracking
- Input validation for monetary amounts
- Account lockout after 3 failed PIN attempts

## Code Structure

### ATMSystem Class

```python
class ATMSystem:
    - __init__(pin, initial_balance)      # Initialize ATM
    - verify_pin(entered_pin)             # Verify PIN
    - deposit(amount)                     # Deposit money
    - withdraw(amount)                    # Withdraw money
    - check_balance()                     # Check balance
    - display_menu()                      # Show menu
    - show_transaction_history()          # Show transactions
    - run()                               # Main loop
```

## Customization

You can easily modify the default PIN and initial balance:

```python
# Change PIN and initial balance
atm = ATMSystem(pin="9999", initial_balance=10000)
atm.run()
```

## Future Enhancements

- Multi-user support
- Database integration
- Account types (Savings, Checking)
- Interest calculation
- Mini statement generation
- Fund transfer between accounts

## License

This project is open source and available under the MIT License.

## Author

Created by: ankithkumarreddyk24cs-bit

## Contributing

Feel free to fork this repository and submit pull requests for any improvements!

---

**Enjoy using the ATM Management System!** 🏦

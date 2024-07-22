# Bank Account Management System

# Day 2 100 days of code

A simple Python program to manage bank accounts, including functionalities for depositing money, transferring funds, and checking account details and transaction history.

## Features

- Create a bank account with first name, last name, and email
- Deposit money into the account
- Transfer money to another bank
- Check account balance
- View statement of account (all transactions)
- View deposit history
- View transfer history
- View account details

## Usage

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-username/bank-account-management.git
    cd bank-account-management
    ```

2. **Run the program**

    ```bash
    python bank.py
    ```

3. **Follow the prompts**

    ```plaintext
    BISHOP's BANK

    Enter your firstname : John
    Enter your lastname : Doe
    Enter your email : john.doe@example.com

    Name -> John Doe,
    Email -> john.doe@example.com,
    Account Number -> 1000012345,
    Balance -> 0

    1. Deposit
    2. Transfer
    3. Check Balance
    4. Check Statement of Account
    5. Check Deposit History
    6. Check Transfer History
    7. Check Account Details
    8. Print this help
    9. Exit the bank

    Enter Your choice in numbers (e.g 1, 2) :
    ```

## Code Explanation

The `Bank` class is defined with several methods to manage a bank account:

- `__init__(self, firstname, lastname, email)`: Initializes a new bank account with the provided first name, last name, and email. Generates a random account number and sets the initial balance to 0.
- `deposit(self, amount)`: Deposits the specified amount into the account and records the transaction.
- `transfer(self, amount, recipientBank)`: Transfers the specified amount to another bank if there are sufficient funds and records the transaction.
- `checkStatementAccount(self)`: Prints all transactions.
- `checkDeposits(self)`: Prints the history of deposits.
- `checkTransfers(self)`: Prints the history of transfers.
- `checkBalance(self)`: Prints the current account balance.
- `checkAccountDetails(self)`: Prints the account details.
- `__str__(self)`: Returns a string representation of the account details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

If you have any questions, feel free to contact me at [odedeyibishop@gmail.com](mailto:odedeyibishop@gmail.com).

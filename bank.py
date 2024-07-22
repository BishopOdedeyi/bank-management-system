import random

class Bank:
    lastAccountNumber = 1000000000
    deposits = []
    transfers = []
    transactions = []

    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = self.firstname + " " + self.lastname
        self.email = email
        self.accountBalance = 0
        self.accountNumber = self.lastAccountNumber + random.randrange(11111, 99999)

    def deposit(self, amount):
        self.accountBalance += amount
        text = f"added {amount}"
        self.deposits.append(text)
        self.transactions.append(text)
        print(text)


    def transfer(self, amount, recipientBank):
        if self.accountBalance != 0:
            self.accountBalance -= amount
            text = f"transferred {amount} to {recipientBank}"
            self.transfers.append(text)
            self.transactions.append(text)
            print(text)
        else:
            print("You dont have up to that amount add more money")

    def checkStatementAccount(self):
        for transaction in self.transactions:
            print(transaction)

    def checkDeposits(self):
        for deposit in self.deposits:
            print(deposit)

    def checkTransfers(self):
        for transfer in self.transfers:
            print(transfer)

    def checkBalance(self):
        print(self.accountBalance)

    def checkAccountDetails(self):
        print(f"\nName -> {self.fullname},\nEmail -> {self.email},\nAccount Number -> {self.accountNumber},\nBalance -> {self.accountBalance}")

    def __str__(self):
        return f"\nName -> {self.fullname},\nEmail -> {self.email},\nAccount Number -> {self.accountNumber},\nBalance -> {self.accountBalance}"

bankName = "BISHOP's BANK"
print(bankName)

help = """

1. Deposit
2. Transer
3. Check Balance
4. Check Statement of Account
5. Check Deposit History
6. Check Transfer History
7. Check Account Details
8. Print this help
9. Exit the bank

"""

firstname = str(input("Enter your firstname : "))
lastname = str(input("Enter your lastname : "))
email = str(input("Enter your email : "))

customer = Bank(firstname=firstname, lastname=lastname, email=email)
print(customer)

print(help)

while True:
    choice = int(input("Enter Your choice in numbers (e.g 1, 2) : "))
    if choice == 1:
        amount = int(input("Please enter the amount you would like to deposit in numbers : "))
        customer.deposit(amount=amount)

    elif choice == 2:
        amount = int(input("Please enter the amount you would like to transfer in numbers : "))
        recipientBank = str(input("Please enter the recipient bank name : "))
        customer.transfer(amount=amount, recipientBank=recipientBank)

    elif choice == 3:
        customer.checkBalance()

    elif choice == 4:
        customer.checkStatementAccount()

    elif choice == 5:
        customer.checkDeposits()

    elif choice == 6:
        customer.checkTransfers()

    elif choice == 7:
        customer.checkAccountDetails()

    elif choice == 8:
        print(help)

    elif choice == 9:
        break
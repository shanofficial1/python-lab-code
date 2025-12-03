class BankAccount:
    def __init__(self, name, acc_no, acc_type, balance):
        self.name = name
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("\nAccount Details")
        print("-------------------")
        print("Depositor Name :", self.name)
        print("Account Number :", self.acc_no)
        print("Account Type   :", self.acc_type)
        print("Balance        :", self.balance)


# Main program
name = input("Enter depositor name: ")
acc_no = input("Enter account number: ")
acc_type = input("Enter account type (Savings/Current): ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, acc_no, acc_type, balance)

account.display()

deposit_amount = float(input("\nEnter amount to deposit: "))
account.deposit(deposit_amount)
account.display()

withdraw_amount = float(input("\nEnter amount to withdraw: "))
account.withdraw(withdraw_amount)
account.display()

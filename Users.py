class User():
    def __init__(self, name, address, email, amount) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.__balance = amount
        self.__transaction_number = 0
        self.__transaction_history = {}
        self.__loan = 0

    def deposit(self, bank, amount):
        self.__balance += amount
        self.__transaction_number += 1
        bank.total_bank_amount += amount

        key = f'Transaction_Num-{self.__transaction_number}(Depositted)'
        self.__transaction_history[key] = amount
        print(f'Hello {self.name}, {amount} deposited successfully in your account')

    def check_balance(self):
        return self.__balance
    
    def check_loan(self):
        return self.__loan
    
    def add_loan(self, amount):
        self.__loan += amount

    def withdraw(self, bank, amount, isBankrupt = False):
        if isBankrupt == True and amount < self.__balance:
           print("The bank is bankrupt")
        else:
            if self.__balance < amount:
                print(f'Not enough money. You have just {self.__balance} Taka')
            else:
                self.__balance -= amount
                self.__transaction_number += 1
                bank.total_bank_amount -= amount
                key = f'Transaction_Num-{self.__transaction_number}(Withdrawn)'
                self.__transaction_history[key] = amount
                print(f'{amount} has successfully withdrawn. Enjoy!')

    def balance_transfer(self, amount, user):
        if self.__balance < amount:
            print("Not enought money. Please deposit first")
        else:
            user.__balance += amount
            self.__balance -= amount
            self.__transaction_number += 1
            user.__transaction_number += 1
            self_key = f'Transaction_Num-{self.__transaction_number}(Transferred)'
            user_key = f'Transaction_Num-{user.__transaction_number}(Recieved)'

            self.__transaction_history[self_key] = amount
            user.__transaction_history[user_key] = amount
            print(f'Hello, {self.name}, you have transferred {amount} taka to {user.name}s bank account')

    def show_transaction(self):
        if self.__transaction_history == {}:
            print(f'No transaction found in {self.name}s account!')
        else:
            print(f'{self.name}s account transaction: ')
            for key, value in self.__transaction_history.items():
                print(f'{key}: {value} Taka')

    def request_loan(self, amount):
        amount += self.loan

    
    def __repr__(self) -> str:
        print(f'{self.name} has {self.__balance} taka in the bank account.')
        return ''
        





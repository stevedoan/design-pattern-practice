from abc import ABC, abstractmethod

class SavingAccountStrategy(ABC):
    @abstractmethod
    def calculate_interest(self, rate):
        pass


class AccountStrategy(ABC):
    @abstractmethod
    def get_account_info(self, amount: float):
        pass

    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def transfer(self, amount: float, target_account: AccountStrategy):
        pass

    @abstractmethod
    def receive(self, amount: float, source_account: AccountStrategy):
        pass


class Account(AccountStrategy):
    def __init__(self, account_name: str, account_number: str, init_amount: float = 0):
        self.account_name = account_name
        self.account_number = account_number
        self.amount = init_amount

    def get_account_info(self):
        print(f'Account Name: {self.account_name} - Account Number: {self.account_number} - Amount: {self.amount}')

    def deposit(self, amount):
        self.amount += amount
    
    def withdraw(self, amount):
        self.amount -= amount

    def transfer(self, amount, target_account):
        self.amount -= amount
        target_account.receive(amount, self)

    def receive(self, amount):
        self.amount += amount

class SavingAccount(Account, SavingAccountStrategy):
    def __init__(self, account_name: str, account_number: str, init_amount: float = 0):
        Account.__init__(self, account_name, account_number, init_amount)

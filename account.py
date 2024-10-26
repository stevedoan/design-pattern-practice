from abc import ABC, abstractmethod


class AccountStrategy(ABC):
    @abstractmethod
    def get_account_info(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def transfer(self, amount, target_account):
        pass

    @abstractmethod
    def receive(self, amount, source_account):
        pass


class SavingAccountStrategy(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass


class CheckingAccountStrategy(ABC):
    @abstractmethod
    def check_overdraft_fee(self):
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
    def __init__(self, account_name: str, account_number: str, interest_rate: float, init_amount: float = 0):
        Account.__init__(self, account_name, account_number, init_amount)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        self.amount += self.amount * self.interest_rate
    

class CheckingAccount(Account, CheckingAccountStrategy):
    def __init__(self, account_name: str, account_number: str, overdraft_rate: float, init_amount: float = 0):
        Account.__init__(account_name, account_number, init_amount)
        self.overdraft_fee = 0
        self.overdraft_rate = overdraft_rate

    def deposit(self, amount):
        self.amount += amount - self.overdraft_fee

    def withdraw(self, amount):
        self.amount -= amount
        if self.amount < 0:
            self.overdraft_fee = abs(self.amount)
            self.amount = 0

    def check_overdraft_fee(self):
        return self.overdraft_rate
    

class AccountFactory:
    @staticmethod
    def get_account(account_type: str, account_name: str, account_number: str, rate: float, init_amount: float = 0):
        if account_type == "saving":
            return SavingAccount(account_name, account_number, rate, init_amount)
        elif account_type == "checking":
            return CheckingAccount(account_name, account_number, rate, init_amount)
        else:
            raise ValueError(f"Unknown account type: {account_type}")

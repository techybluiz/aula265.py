import abc

class Account(abc.ABC):
    def __init__(self, agency: int, account: int, money: float=0) -> None:
        self.agency = agency
        self.account = account
        self.money = money
        
    @abc.abstractmethod
    def withdraw(self, value: float):
        ...
    def deposit(self, value: float):
        self.money += value
        self.info(f'Deposit {value}')
        return self.money
    def info(self, msg: str = '') -> None:
        print(f'Your balance is {self.money:.2f} {msg}')
        print('--')
        
    def __repr__(self) -> str:
        class_name = type (self).__name__
        attrs = f'({self.agency!r}, {self.account!r}, {self.money!r})'
        return f'{class_name}{attrs}'

class SavingAccount(Account):
    def withdraw(self, value: float):
        after_withdraw = self.money - value
        
        if after_withdraw >= 0:
            self.money -= value
            self.info(f'(Withdraw {value})')
            return self.money
        
        print('Unable to withdraw the desired amount')
        self.info(f'(WITHDRAWAL DENIED {value})')
        return self.money

class CurrentAccount(Account):
    def __init__ (
        self, agency: int, account: int,
        money: float = 0, limit: float = 0
    ):
        super().__init__(agency, account, money)
        self.limit = limit
        
    def withdraw(self, value: float):
        after_withdraw = self.money - value
        max_limit = -self.limit
        
        if after_withdraw >= max_limit:
            self.money -= value
            self.info(f'(Withdraw {value})')
            return self.money
        
        print('Unable to withdraw the desired amount')
        print(f'Your limit is {-self.limit:.2f}')
        self.info(f'(WITHDRAWAL DENIED {value})')
        return self.money
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.account!r}, {self.money!r}, {self.limit!r})'
        return f'{class_name} {attrs}'
    
if __name__ == '__main__':
    cp1 = SavingAccount(111,222)
    cp1.withdraw(1)
    cp1.deposit(1)
    print('####')
    cc1 = CurrentAccount(111,222,0,100)
    cc1.withdraw(1)
    cc1.deposit(98)
    print('####')
    

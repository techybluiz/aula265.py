class Bank:
    def __init__(
        self,
        agencies: list[int] | None = None,
        client: list[people.Person] | None = None,
        accounts: list[accounts.Account] | None = None,
    ):
        self.agencies = agencies or []
        self.client = client or []
        self.accounts = accounts or []

    def _check_agency(self, account):
        if account.agency in self.agencies:
            print('_check_agency', True)
            return True
        print('_check_agency', False)
        return False

    def _check_client(self, client):
        if client in self.client:
            print('_check_client', True)
            return True
        print('_check_client', False)
        return False

    def _check_account(self, account):
        if account in self.accounts:
            print('_check_account', True)
            return True
        print('_check_account', False)
        return False

    def _check_your_account_client(self, client, account):
        if account is client.account:
            print('_check_your_account_client', True)
            return True
        print('_check_your_account_client', False)
        return False

    def authenticate(self, client: people.Person, account: accounts.Conta):
        return self._check_agency(account) and \
            self._check_client(client) and \
            self._check_account(account) and \
            self._check_your_account_client(client, account)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencies!r}, {self.client!r}, {self.accounts!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c1 = people.Client('Luiz', 30)
    cc1 = accounts.CheckingAccount(111, 222, 0, 0)
    c1.account = cc1
    c2 = people.Client('Maria', 18)
    cp1 = accounts.SavingsAccount(112, 223, 100)
    c2.account = cp1
    bank = Bank()
    bank.client.extend([c1, c2])
    bank.accounts.extend([cc1, cp1])
    bank.agencies.extend([111, 222])

    if bank.authenticate(c1, cc1):
        cc1.deposit(10)
        c1.account.deposit(100)
        print(c1.account)

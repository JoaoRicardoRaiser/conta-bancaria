from app.user.User import User


class Bank:
    def __init__(self, name):
        self._name = name
        self._accounts = []
        self._users_accounts_registration = []

    def get_bank_name(self):
        return self._name

    def create_login(self) -> str:
        pass

    def create_account(self) -> User:
        return self.accounts.append(User())
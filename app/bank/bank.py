from app.user.User import User


class Bank:
    def __init__(self):
        self._accounts = []
        self._users_accounts_registration = []

    def create_login(self) -> str:
        pass

    def create_account(self) -> User:
        return self.accounts.append(User())
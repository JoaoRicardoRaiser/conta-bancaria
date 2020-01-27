from app.bank.login.login_user import LoginUser


class UserAccount(LoginUser):
    def __init__(self, number, agency, bank, login: LoginUser):
        self._number = number
        self._agency = agency
        self._bank = bank
        self._login = login

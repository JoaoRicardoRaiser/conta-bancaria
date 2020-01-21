from app.bank.account.user_account import BankAccount
from app.bank.login.login_user import LoginUser


class User:
    def __init__(self, name: str, cpf: str, bank_account: BankAccount, login_user: LoginUser):
        self._complete_name = name
        self._cpf = cpf
        self._bank_account = bank_account
        self._login_user = login_user

    def __repr__(self) -> str:
        return f"{self._complete_name}, {self._cpf}, {self._bank_account}, {self._login_user}"

    def get_complete_name(self) -> str:
        return self._complete_name

    def get_cpf(self) -> str:
        return self._cpf

    def get_bank_account(self) -> BankAccount:
        return self._bank_account

    def get_login_user(self) -> LoginUser:
        return self._login_user
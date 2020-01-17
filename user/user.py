

class User:
    def __init__(self, name: str, cpf: str, bank_account: BankAccount, login_user: LoginUser):
        self._name = name
        self._cpf = cpf
        self._bank_account = bank_account
        self._login_user = login_user

# Pintar letras do terminal
# print('\033[1;32mHello word\033[m')

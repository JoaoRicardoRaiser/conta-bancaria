from unittest.mock import patch, MagicMock
import unittest

from app.bank.account.user_account import BankAccount
from app.bank.login.login_user import LoginUser
from app.user.User import User


class TestUser(unittest.TestCase):
    def test_user_have_all_atributes(self):
        # arrange
        bank_account_mock = BankAccount('1234567890', '105', 'Bradesco')
        cpf = MagicMock(return_value='22073303110')
        login_mock = LoginUser('guikramer', '260997')

        user = User('Guilherme Kramer', 'gui.kramer@hbsis.com.br', cpf, bank_account_mock, login_mock)

        self.assertEqual(user.get_complete_name(), 'Guilherme Kramer')
        self.assertEqual(user.get_email(), 'gui.kramer@hbsis.com.br')
        self.assertEqual(user.get_cpf(), cpf)
        self.assertEqual(user.get_login_user(), login_mock)
        self.assertIsInstance(bank_account_mock, BankAccount)
        self.assertIsInstance(login_mock, LoginUser)
        self.assertIsInstance(user, User)

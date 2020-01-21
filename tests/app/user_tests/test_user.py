from unittest.mock import patch, MagicMock
import unittest
from app.user.User import User


class TestUser(unittest.TestCase):
    pass
    # @patch('app.user.User.login')
    # @patch('app.user.User.cpf')
    # @patch('app.user.User.bank_account')
    # def test_user_have_all_atributes(self, bank_account_mock, cpf_mock, login_mock):
    #     #arrange
    #     bank_account_mock.return_value = '1234567890'
    #     cpf_mock.return_value = '22073303110'
    #     login_mock.return_value = 'Guikramer'
    #
    #     user = User('Guilherme Kramer', bank_account_mock,cpf_mock, login_mock)
    #
    #     self.assertEqual(user, User())

    # nada a ver esse teste, to fumando cotonete
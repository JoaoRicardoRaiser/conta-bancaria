class LoginUser:
    def __init__(self, user_name: str, password: str):
        self._user_name = user_name
        self._password = password

    def get_user_name(self):
        return self._user_name

    def get_password(self):
        return self._password

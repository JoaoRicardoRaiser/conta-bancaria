
class LoginUser:
    def __init__(self, user_name: str, password: str):
        self._user_name = user_name
        self._password = password


# poderiamos fazer essa classe como session, ela receberia um user e faria o login
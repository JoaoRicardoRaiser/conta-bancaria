from app.home_page.screen import Screen


class Response:
    _list_responses: list = ['1', '2', '3', '4', '5']

    def is_valid(self, value: str):
        return True if value in self._list_responses else None


screen = Screen()
response = Response()
screen.show_logged_screen()
result = response.is_valid(input('Opção: '))
while not result:
    print('A opção não é válida')
    screen.show_logged_screen()
    result = response.is_valid(input('Opção: '))

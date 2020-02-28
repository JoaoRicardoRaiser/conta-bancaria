class Screen:
    def __print_word(self, word, color):
        if color == 'verde':
            return (f'\033[1;32m{word}\033[m')

    def show_logged_screen(self):
        return (print('=' * 60),
                print(f'Seja Bem Vindo ao banco {self.__print_word("Bradesco", "verde")}'),
                print('Escolha (com apenas números) a opção desejada: \n'
                      '* 1 - Saque\n'
                      '* 2 - Depósito\n'
                      '* 3 - Transferência\n'
                      '* 4 - Saldo\n'
                      '* 5 - Sair'),
                print('=' * 60))



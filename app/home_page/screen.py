

def print_word(word,color):
    if color == 'verde':
        return(f'\033[1;32m{word}\033[m')


def show_screen():
    print('Escolha (com apenas números) a opção desejada: \n'
          '* 1 - Saque\n'
          '* 2 - Depósito\n'
          '* 3 - Transferência\n'
          '* 4 - Saldo\n'
          '* 5 - Sair')


print('='*60)
print('Seja bem Vindo ao banco ' + print_word('Bradesco', 'verde'))
show_screen()




def pintar_palavra(palavra,cor):
    if cor == 'verde':
        return(f'\033[1;32m{palavra}\033[m')



print('='*60)
print('Seja bem Vindo ao banco ' + pintar_palavra('Bradesco', 'verde'))
print('Escolha (com apenas números) a sua opção:')
print('1 -')

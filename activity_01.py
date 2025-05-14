# simula calculadora
import random


def ad_nums(t1, t2):
    'adição entre dois termos'
    ad = t1 + t2
    return ad


def dif_nums(t1, t2):
    'subtração entre dois termos'
    dif = t1 - t2
    return dif


def prod_nums(t1, t2):
    'multiplicação entre dois termos'
    prod = t1 * t2
    return prod


def div_nums(t1, t2):
    'divisão entre dois termos'
    div = t1 / t2
    return div


def exp_nums(t1, t2):
    'potenciação entre dois termos'
    exp = t1 ** t2
    return exp


def root_nums(t1, t2):
    'radiciação entre dois termos'
    root = t1 ** (1 / t2)
    return root


print(89*'_'+'\n')
print(26*' '+' Bem vindo a calculadora do Nicao-ps '+26*' ')

function = ''

while True:
    print(89*'_'+'\n')
    print('Selecione uma das opções disponíveis:\n')
    print('1 - Adição  | 2 - Subtração   | 3 - Multiplicação')
    print('4 - Divisão | 5 - Potenciação | 6 - Radiciação')
    print('0 - Para sair')
    print(89*'_'+'\n')
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    function = int(input('Informe a opção: '))
    match function:
        case 0:
            print('\nGoodbye! :)')
            break
        case 1:
            print(f'\n{n1} + {n2} = {ad_nums(n1, n2)}')
        case 2:
            print(f'\n{n1} - {n2} = {dif_nums(n1, n2)}')
        case 3:
            print(f'\n{n1} * {n2} = {prod_nums(n1, n2)}')
        case 4:
            print(f'\n{n1} / {n2} = {div_nums(n1, n2)}')
        case 5:
            print(f'\n{n1} ** {n2} = {exp_nums(n1, n2)}')
        case 6:
            print(f'\n{n1} ** (1/{n2}) = {root_nums(n1, n2)}')
        case _:
            print('\nOpção Inválida. Selecione uma opção válida entre 0 e 6.')

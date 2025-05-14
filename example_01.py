# Gera números aleatórios
import random
import os

os.system('cls')


def generate_numbers(i, f, q):
    'Gera números'
    list_numbers = [random.randint(i, f) for num in range(q)]
    return list_numbers


inicial = int((input('Informe o primeiro número: ')))
final = int((input('Informe o último número: ')))
qtty = int((input('Quantos números? ')))


numbers = generate_numbers(inicial, final, qtty)
print(numbers)

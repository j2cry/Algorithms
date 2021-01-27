# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

from string import ascii_lowercase

char = input('Enter char: ')

pos = ascii_lowercase.find(char.lower()) + 1

print(f'Char "{char}" position: {pos}')

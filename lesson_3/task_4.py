# Определить, какое число в массиве встречается чаще всего.

source = [10, 15, 22, 41, 3, 14, 10, 13, 22, 7, 7, 7, 41, 19, 10, 7, 93, 11, 7, 14, 22, 7]

max_counter = 1
num = 0

for index in range(len(source) - 1):
    counter = 1
    for compare_index in range(index + 1, len(source)):
        counter += bool(source[index] == source[compare_index])
    if max_counter < counter:
        max_counter = counter
        num = source[index]

print(f'Number {num} occurs {max_counter} times in the sequence')

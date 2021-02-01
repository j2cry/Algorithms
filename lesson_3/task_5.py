# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

source = [-20, -13, 17, 8, 3, -6, 1, 11, 15, -7, -3, -19]
result = source[0]
result_index = 0

for index in range(len(source)):
    if (source[index] < 0) and (abs(source[index]) < abs(result)):
        result = source[index]
        result_index = index

print(f'Max negative = {result}, index = {result_index}')

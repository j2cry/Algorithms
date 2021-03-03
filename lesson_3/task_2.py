# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
# со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация
# начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.

source = [3, 7, 4, 9, 12, 35, 22, 76, 13, 88, 514]
result = [index for index, elem in enumerate(source) if elem % 2 == 0]

# for index, num in enumerate(source):
#     if num % 2 == 0:
#         result.append(index)

print(result)
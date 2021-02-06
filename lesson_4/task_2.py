# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена». Второй — без использования «Решета Эратосфена».

# алгоритмы 1, 3 и 4 - суть одно и то же, с разницей в проверке делимости:
# в 1-ом перебор всех простых делителей до первого нахождения
# во 2-ом перебор любых делителей до первого нахождения
# в 3-ем перебор всех найденных простых делителей
# в 4-ом перебор всех найденных простых делителей меньше корня из n, до первого нахождения

from itertools import count
from math import sqrt
from task_1 import test_algorithm

target = 500


def algorithm_1():
    primes = [2]

    for number in count(3):     # start from 3, cause 2 is already known as prime number
        for prime in primes:    # check whether the current number is divisible by all prime numbers before it
            if number % prime == 0:
                break       # divisor found
        else:
            primes.append(number)
            if len(primes) >= target:
                break
    return f'The {target}-th prime number is {primes[-1]}'


def algorithm_2():     # another way to check divisibility
    primes = [2]

    for number in count(3):     # start from 3, cause 2 is already known as prime number
        # check whether the current number is divisible by all prime numbers before it
        divisible = any([number % prime == 0 for prime in primes])
        if not divisible:
            primes.append(number)
        if len(primes) == target:        # break if target number was found
            break
    return f'The {target}-th prime number is {primes[-1]}'


def algorithm_3():     # iterating through divisors
    primes = [2]

    for number in count(3):
        for divisor in range(2, number):
            if number % divisor == 0:       # divisor found => number is not prime
                break
        else:
            primes.append(number)
        if len(primes) == target:        # break if target number was found
            break
    return f'The {target}-th prime number is {primes[-1]}'


def algorithm_4():
    primes = [2]

    for number in count(3):     # start from 3, cause 2 is already known as prime number
        # check whether the current number is divisible by all prime numbers before it
        for prime in [pr for pr in primes if pr <= sqrt(number)]:
            if number % prime == 0:
                break       # divisor found
        else:
            primes.append(number)
            if len(primes) >= target:
                break
    return f'The {target}-th prime number is {primes[-1]}'


if __name__ == '__main__':
    print(algorithm_1())
    print(algorithm_2())
    print(algorithm_3())
    print(algorithm_4())
    test_algorithm(algorithm_1, algorithm_2, algorithm_3, algorithm_4, loops=100)


# OUTPUT:
# Algorithm 1, loops = 100:
#     minimal time: 0.004914900000000055
#     maximal time: 0.01120869999999996
#     average time: 0.006126780999999995
#     median time: 0.0056600500000000276
# ------
# Algorithm 2, loops = 100:
#     minimal time: 0.046858100000000125
#     maximal time: 0.06956209999999996
#     average time: 0.05066537199999997
#     median time: 0.049133249999999684
# ------
# Algorithm 3, loops = 100:
#     minimal time: 0.032754900000000475
#     maximal time: 0.07156370000000045
#     average time: 0.03833916000000004
#     median time: 0.036044550000000175
# ------
# Algorithm 4, loops = 100:
#     minimal time: 0.12089019999999984
#     maximal time: 0.1828333000000022
#     average time: 0.13561931099999996
#     median time: 0.13738525000000124
# ------
# The best algorithm is 1 with avg. time 0.006126780999999995
#    It is 8.26949290336965 times faster than algorithm 2
#    It is 6.257635126830887 times faster than algorithm 3
#    It is 22.135491867589206 times faster than algorithm 4

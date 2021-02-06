# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена». Второй — без использования «Решета Эратосфена».

# Алгоритмы:
# в 1-ом перебор всех простых делителей до первого успешного деления; сложность O(N) ?
# во 2-ом перебор вообще всех делителей до первого успешного деления; сложность O(N^2)
# в 3-ем перебор всех простых делителей меньше корня из number, до первого успешного деления; сложность тоже O(N)?

# если интересно, приложил график скорости работы алгоритмов (сек) в зависимости от дальности искомого числа:
# для i от 1000 до 19000 с шагом 1000

from itertools import count
from math import sqrt
from task_1 import test_algorithm
import cProfile
from timeit import timeit

target = 100


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


def algorithm_2():     # iterating through divisors
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


def algorithm_3():
    primes = [2]

    for number in count(3):     # start from 3, cause 2 is already known as prime number
        # check whether the current number is divisible by prime numbers < sqrt(number)
        sq_num = sqrt(number)
        is_prime = False
        for prime in primes:
            if prime > sq_num:
                is_prime = True
                break       # нет смысла искать дальше
            if number % prime == 0:
                break       # divisor found
        if is_prime:
            primes.append(number)
            if len(primes) >= target:
                break
    return f'The {target}-th prime number is {primes[-1]}'


if __name__ == '__main__':
    print(algorithm_1())
    print(algorithm_2())
    print(algorithm_3())
    test_algorithm(algorithm_1, algorithm_2, algorithm_3, loops=10)

    print('----- Algorithm 1 -----')
    cProfile.run('algorithm_1()')
    print('----- Algorithm 2 -----')
    cProfile.run('algorithm_2()')
    print('----- Algorithm 3 -----')
    cProfile.run('algorithm_3()')

    # lp = 5
    # for trg in range(1, 20):
    #     target = trg * 1000
    #     print(timeit(algorithm_1, number=lp) / lp)

# OUTPUT:
# Algorithm 1, loops = 10:
#     minimal time: 4.4706667000000095
#     maximal time: 4.826662400000004
#     average time: 4.597649979999998
#     median time: 4.572034399999993
# ------
# Algorithm 2, loops = 10:
#     minimal time: 55.0066061
#     maximal time: 62.9543779
#     average time: 59.30017627999999
#     median time: 60.79520400000001
# ------
# Algorithm 3, loops = 10:
#     minimal time: 0.13377830000001723
#     maximal time: 0.1450428999999076
#     average time: 0.13856887999999118
#     median time: 0.13834385000001248
# ------
# The best algorithm is 3 with avg. time 0.13856887999999118
#    It is 33.17952761110785 times faster than algorithm 1
#    It is 427.94728715425686 times faster than algorithm 2
# ----- Algorithm 1 -----
#          30002 function calls in 5.040 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    5.040    5.040 <string>:1(<module>)
#         1    5.035    5.035    5.040    5.040 task_2.py:19(algorithm_1)
#         1    0.000    0.000    5.040    5.040 {built-in method builtins.exec}
#     14999    0.002    0.000    0.002    0.000 {built-in method builtins.len}
#     14999    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# ----- Algorithm 2 -----
#          30002 function calls in 61.376 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   61.376   61.376 <string>:1(<module>)
#         1   61.364   61.364   61.376   61.376 task_2.py:33(algorithm_2)
#         1    0.000    0.000   61.376   61.376 {built-in method builtins.exec}
#     14999    0.005    0.000    0.005    0.000 {built-in method builtins.len}
#     14999    0.007    0.000    0.007    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# ----- Algorithm 3 -----
#          193841 function calls in 0.168 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.168    0.168 <string>:1(<module>)
#         1    0.139    0.139    0.168    0.168 task_2.py:47(algorithm_3)
#         1    0.000    0.000    0.168    0.168 {built-in method builtins.exec}
#     14999    0.002    0.000    0.002    0.000 {built-in method builtins.len}
#    163839    0.026    0.000    0.026    0.000 {built-in method math.sqrt}
#     14999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

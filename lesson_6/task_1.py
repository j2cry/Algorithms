# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# я перепробовал кучу алгоритмов из прошлых уроков, но все они ели памяти +/- одинаково: см. результат
# по задаче 4 из урока 3.
# В задаче с Эратосфеном отличия мне показались более наглядными, поэтому взял её

from itertools import count
from math import sqrt, log
import sys
from memory_profiler import profile


@profile
def algorithm_1(target):
    primes = [2]
    rng = int(1.5 * target * log(target))
    for number in range(3, rng, 2):
        for prime in primes:    # check whether the current number is divisible by all prime numbers before it
            if number % prime == 0:
                break       # divisor found
        else:
            primes.append(number)
            if len(primes) >= target:
                break
    return f'The {target}-th prime number is {primes[-1]}'


@profile
def algorithm_2(target):     # iterating through divisors
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


@profile
def algorithm_3(target):
    primes = [3]
    for number in count(3, 2):     # start from 3, cause 2 is already known as prime number
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
    primes = [2, *primes]
    return f'The {target}-th prime number is {primes[-1]}'


@profile
def algorithm_3_lim(target):
    primes = [3]
    rng = int(1.5 * target * log(target))
    for number in range(3, rng, 2):     # start from 3, cause 2 is already known as prime number
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
    primes = [2, *primes]
    return f'The {target}-th prime number is {primes[-1]}'


# Задание 4 из урока 3 - Определить, какое число в массиве встречается чаще всего.
# v1
@profile
def additional_1(source):
    max_counter = 1
    number = 0
    for index in range(len(source) - 1):
        counter = 1
        for compare_index in range(index + 1, len(source)):
            counter += bool(source[index] == source[compare_index])
        if max_counter < counter:
            max_counter = counter
            number = source[index]
    print(f'Number {number} occurs {max_counter} times in the sequence')


# v2
@profile
def additional_2(source):
    max_counter = 1
    number = 0
    counter = {}
    for num in source:
        if counter.get(num):
            counter[num] += 1
        else:
            counter.update({num: 1})

    for num, cnt in counter.items():
        if max_counter < cnt:
            max_counter = cnt
            number = num
    print(f'Number {number} occurs {max_counter} times in the sequence')


# просто ради интереса: задание 7 урока 3
@profile
def les_3_t_7(source: list):
    first_min, second_min = source[0], source[0]
    for index in range(len(source)):
        if source[index] <= first_min:
            second_min = first_min
            first_min = source[index]
            continue
        if source[index] < second_min:
            second_min = source[index]
    print(f'Two smallest values: {first_min}, {second_min}')


if __name__ == '__main__':
    print(sys.version, sys.platform)
    n = 500
    print('ALG 1:', algorithm_1(n))
    print('ALG 2:', algorithm_2(n))
    print('ALG 3:', algorithm_3(n))
    print('ALG 3 lim:', algorithm_3_lim(n))
    print('-' * 50)

    data = [10, 15, 41, 3, -80, -13, 17, 8, 3, -6, 1, 11, 15, -7, -3, -19, 10, 7, 93, 11, 7, 14, 22, 7]
    additional_1(data)
    additional_2(data)
    les_3_t_7(data)

# Выводы:
# 0) под все объекты скрипта выделено примерно 20 МиБ
# 1) При малых значениях target все алгоритмы равноценны
# 2) при высоких значениях target алгоритм 3 занимает памяти как будто бы чуть меньше и освобождает её раньше
# 3) алгоритмы первых трех уроков неинтересно рассматривать с точки зрения использования памяти
#       в виду отсутствия динамики


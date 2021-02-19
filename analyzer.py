import tracemalloc
from functools import partial
from timeit import timeit
from statistics import median
from typing import Union, Tuple
from collections import namedtuple
from random import randint, uniform

Bounds = namedtuple('Bounds', 'lower, upper')


def print_analyze(func):
    def wrapper(*args, **kwargs):
        # Setting the flag that the wrapper of function with this name is already being executed
        if getattr(wrapper, 'running', False):
            return func(*args)
        else:
            setattr(wrapper, 'running', True)

        func_name = func.__name__
        loops = 10
        print('=' * 75)
        tracemalloc.clear_traces()
        result = func(*args)
        current, peak = tracemalloc.get_traced_memory()
        print(f'[{func_name}] MEMORY: {current} | {peak}')
        times = [timeit(partial(func, *args, **kwargs), number=loops) for _ in range(loops)]
        print(f'[{func_name}] TIME: {median(times)} per loop | {loops} loops')
        print(f'[{func_name}] RESULT: ', end='')
        return result

    tracemalloc.start()
    return wrapper


def values(bounds: Tuple[Union[int, float], Union[int, float]], count: int, dig_round=3):
    """ Generate list of values """
    if count < 1:
        count = 1
    bounds = Bounds(bounds[0], bounds[1])
    if isinstance(bounds.lower, float) or isinstance(bounds.upper, float):
        return [round(uniform(bounds.lower, bounds.upper - 10 ** -dig_round), dig_round) for _ in range(count)]
    elif isinstance(bounds.lower, int) and isinstance(bounds.upper, int):
        return [randint(bounds.lower, bounds.upper - 1) for _ in range(count)]

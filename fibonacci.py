import numpy as np
import pandas as pd
import timeit


def fibonacci_0(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    fibs = [0, 1, 1]
    i = 2
    while i <= (n - 1):
        fibs.append(fibs[-2] + fibs[-1])
        i += 1
    return fibs


def fibonacci_1(n):
    if n == 0:
        return [0]
    fibs = [0, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def fibonacci_2(n):
    fibs = [0, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[-2] + fibs[-1])
    return fibs[:(n + 1)]


def fibonacci_3(n):
    fibs = [0, 1] + [None] * (n - 1)
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 2] + fibs[i - 1]
    return fibs[:(n + 1)]


def fibonacci_4(n):
    if n == 0:
        return [0]
    fibs = {0: 0, 1: 1}
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs.values()


def fibonacci_5(n):
    if n == 0:
        return [0]
    fibs = [0]
    temp = {0: 0, 1: 1}
    for _ in range(1, n + 1):
        temp[_ % 2] = temp[0] + temp[1]
        fibs.append(temp[_ % 2])
    return fibs


def fibonacci_6(n):
    fibs = [0, 1]
    if n == 0:
        return [0]
    elif n == len(fibs):
        return fibs
    elif n > len(fibs):
        for i in range(len(fibs), n + 1):
            fibs.append(fibs[-1] + fibs[-2])
        return fibs
    elif n < len(fibs):
        fibs2 = [0, 1]
        for i in range(2, n + 1):
            fibs2.append(fibs2[i - 1] + fibs2[i - 2])
        return fibs2


def memorise(f):
    results = {0: [0], 1: [0, 1]}

    def worker(x):
        try:
            return results[x]
        except BaseException:
            tmp = f(x)
            results[x] = tmp
            return tmp
    return worker


@memorise
def fibonacci_7(n):
    r1, r2 = 0, 1
    fibs = [0, 1]
    listappend = fibs.append
    for i in range(2, n + 1):
        fib = r1 + r2
        listappend(fib)
        r1, r2 = r2, fib
    return fibs


if __name__ == '__main__':

    ranks_algos = []
    df = pd.DataFrame(columns=[
        'algorithm',
        'lower_bound_time'])

    for i in range(0, 8):
        name = 'fibonacci_' + str(i)
        print(name)

        # https://docs.python.org/3.2/library/timeit.html
        times = timeit.repeat(
            name + "(1000)",
            repeat=100,
            number=100,
            setup="from __main__ import " + name)

        min_t = np.min(times)
        l = [name, min_t]
        ranks_algos.append(l)

    df = df.append(
        pd.DataFrame(ranks_algos, columns=df.columns))

    print(df)

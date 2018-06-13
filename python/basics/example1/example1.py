import random
import timeit
import math
import sys

def mean(lst):
    return sum(lst) / len(lst)


def standard_deviation(lst):
    m = mean(lst)
    variance = sum([(value - m) ** 2 for value in lst])
    return math.sqrt(variance / len(lst))

if __name__ == '__main__':

    lens = range(10, 300, 10)
    py_time = []

    for l in lens:
        rands = [random.random() for _ in range(0, l)]
        execution_time = timeit.timeit(lambda: standard_deviation(rands), number=10000)
        py_time.append(execution_time)
        print("array_size: %3d, execution_time:%f" % (l, execution_time))

    with open("data/time_per_array_size.dat", "w") as f:
        for i in range(len(py_time)):
            f.write("%d %f\n" % (lens[i], py_time[i]))

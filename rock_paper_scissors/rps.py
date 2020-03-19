#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    cache = {i: 3 ** i for i in range(n + 1)}
    conditions = ['rock', 'paper', 'scissors']
    my_list = [[] for _ in range(cache[n])]
    rps_generator(n, my_list, conditions, n, cache)
    return my_list


def rps_generator(current_n, return_list, conditions, target, cache, x=0):
    if current_n < 1:
        return return_list
    index = [0, 1, 2]
    indexes = [ele for ele in index for i in range(cache[current_n - 1])]
    if current_n != target:
        indexes *= len(return_list) // len(indexes)
    for i in range(3 ** target):
        return_list[i].append(conditions[indexes[i]])
    rps_generator(current_n - 1, return_list, conditions, target, cache, x+1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

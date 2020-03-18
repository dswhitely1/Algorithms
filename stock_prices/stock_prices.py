#!/usr/bin/python

'''
You want to write a bot that will automate the task of day-trading for you while you're going through Lambda. 
You decide to have your bot just focus on buying and selling Amazon stock.

Write a function find_max_profit that receives as input a list of stock prices. Your function should return
the maximum profit that can be made from a single buy and sell. 
You must buy first before selling; no shorting is allowed here.

For example, find_max_profit([1050, 270, 1540, 3800, 2]) should return 3530, which is the maximum profit
that can be made from a single buy and then sell of these stock prices.
'''
import argparse


def merge(a, b):
    x = y = 0
    result = []
    while x < len(a) and y < len(b):
        if a[x] < b[y]:
            result.append(a[x])
            x += 1
        else:
            result.append(b[y])
            y += 1

    result.extend(a[x:])
    result.extend(b[y:])

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    point = len(arr) // 2

    lhs = merge_sort(arr[point:])
    rhs = merge_sort(arr[:point])

    return merge(lhs, rhs)


def find_max_profit(prices):
    min_value = prices[0]
    difference = []
    for i in range(1, len(prices)):

        result = prices[i] - min_value

        if min_value > prices[i]:
            min_value = prices[i]
        difference.append(result)

    sorted_difference = merge_sort(difference)

    return sorted_difference[len(sorted_difference) - 1]


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

#!/usr/bin/python

"""
You want to write a bot that will automate the task of day-trading for you while you're going through Lambda.
You decide to have your bot just focus on buying and selling Amazon stock.

Write a function find_max_profit that receives as input a list of stock prices. Your function should return
the maximum profit that can be made from a single buy and sell.
You must buy first before selling; no shorting is allowed here.

For example, find_max_profit([1050, 270, 1540, 3800, 2]) should return 3530, which is the maximum profit
that can be made from a single buy and then sell of these stock prices.
"""
import argparse


# def merge(a, b):
#     x = y = 0
#     result = []
#     while x < len(a) and y < len(b):
#         if a[x] < b[y]:
#             result.append(a[x])
#             x += 1
#         else:
#             result.append(b[y])
#             y += 1
#
#     result.extend(a[x:])
#     result.extend(b[y:])
#
#     return result
#
#
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     point = len(arr) // 2
#
#     lhs = merge_sort(arr[point:])
#     rhs = merge_sort(arr[:point])
#
#     return merge(lhs, rhs)
#
#
# def find_max_profit(prices):
#     # set Min Value
#     min_value = prices[0]
#     # Set the Difference List
#     difference = []
#     # Loop through List starting at index 1 and subtract list[i] - list[i - 1]
#     for i in range(1, len(prices)):
#         # Get Result of Current Price minus Min Value
#         result = prices[i] - min_value
#         # Set Min Value if it is the new Min Value
#         if min_value > prices[i]:
#             min_value = prices[i]
#         # Append The Result
#         difference.append(result)
#     # Sort the Difference List with Merge Sort Algorithm
#     sorted_difference = merge_sort(difference)
#     # Return the last index of the sorted Array
#     return sorted_difference[-1]

# Second Pass Solution
def find_max_profit(prices, min_value=0, cur_profit=0, index=1):
    if index >= len(prices):
        return cur_profit

    if min_value == 0:
        min_value = prices[0]
        cur_profit = prices[index] - prices[0]

    if prices[index] - min_value > cur_profit:
        cur_profit = prices[index] - min_value

    if min_value > prices[index]:
        min_value = prices[index]

    return find_max_profit(prices, min_value, cur_profit, index + 1)


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

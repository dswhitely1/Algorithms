#!/usr/bin/python

import sys

"""
Cookie Monster can eat either 0, 1, 2, or 3 cookies at a time. If he were given a jar of cookies 
with n cookies inside of it, how many ways could he eat all n cookies in the cookie jar? 
Implement a function eating_cookies that counts the number of possible ways Cookie Monster 
can eat all of the cookies in the jar.

For example, for a jar of cookies with n = 3 (the jar has 3 cookies inside it), 
there are 4 possible ways for Cookie Monster to eat all the cookies inside it:

He can eat 1 cookie at a time 3 times
He can eat 1 cookie, then 2 cookies
He can eat 2 cookies, then 1 cookie
He can eat 3 cookies all at once.
Thus, eating_cookies(3) should return an answer of 4.
"""

# Understand
# n = 0 should return
# n = 1 should return 1
# n = 2 should return 3
# n = 3 should return 4
# n = 4 should return 1 x 4, 1 then 3, 2 then 2, 3 then 1, 4 all at once should return 5
# Possible Solution, count number of stacks for each one
"""
5 + 0 All Cookies
4 + 1
3 + 2 
3 + 1 + 1
2 + 3
2 + 2 + 1
2 + 1 + 1 + 1
1 + 4
1 + 3 + 1
1 + 2 + 2
1 + 2 + 1 + 1
1 + 1 + 1 + 1 + 1

1 + 1 + 1
1 + 2
2 + 1
3 + 0

1 + 1 + 1 + 1
1 + 2 + 1
1 + 1 + 2
1 + 3
2 + 1 + 1
2 + 2
3 + 1
4 + 0
"""


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = {i: 0 for i in range(n+1)}
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
        return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies),
                                                                                    n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')

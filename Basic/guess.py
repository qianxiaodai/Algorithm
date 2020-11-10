# -*- coding: utf-8 -*-
import math
"""
歌德巴赫猜想j
2000以内大于2的偶数能分解为两个素数之和。
"""


def isPrime(n):

    for j in range(2, int(math.sqrt(float(n))) + 1):
        if n % j == 0:
            return False

    return True


def getPrime(n):
    primes = list()
    for j in range(2, n + 1):
        if isPrime(j):
            primes.append(j)

    return primes


# def evenResolution(even, primes):
#     n = len(primes)
#     ans = []
#
#     for i in range(n):
#         # print(primes[i])
#         j = i
#         while j < n:
#             if primes[j] == even - primes[i]:
#                 ans.extend([primes[i], primes[j]])
#                 return ans
#             # print(primes[j])
#
#             elif primes[j] > even - primes[i]:
#                 break
#             j += 1
#     return ans


def evenResolution(even, primes):
    n = len(primes)
    left, right = 0, n - 1
    # ans = []

    while left <= right:
        if primes[left] + primes[right] > even:
            right -= 1

        elif primes[left] + primes[right] < even:
            left += 1

        else:
            return [primes[left], primes[right]]

    return []


if __name__ == '__main__':
    ans = getPrime(1998)
    # print(len(ans))
    # print(ans)

    i = 4

    # res = evenResolution(16, ans)
    # print(res)
    while i <= 2000:
        res = evenResolution(i, ans)
        if res:
            print(f"{i:3d} = {res[0]: 3d} + {res[1]: 3d}")

        else:
            print(f"{i} can't be resolved.")

        i += 2




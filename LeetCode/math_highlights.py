# -*- coding: utf-8 -*-
import math


class Solution:
    """超时"""
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(2, n):
            if self.isPrime(i):
                count += 1
        return count

    def isPrime(self, n: int) -> int:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True


if __name__ == '__main__':
    pass

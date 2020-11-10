# -*- coding: utf-8 -*-

from datetime import datetime
from collections import defaultdict
# 1. 什么地方递归调用本身
# 2. 什么时候终止递归
# "兔子数列"： 后面的数等于前两个数之和
# 1 1 2 3 5 8 13

# 递归
# https://www.jianshu.com/p/b434a5f93d7e

# 生兔子问题
# https://www.cnblogs.com/codingFiend/p/9196655.html

# import timeit 获取稳定的耗时


def fib_test():
   fib_test()


def fib_test(k):
    """求解第k个数的值"""
    k_1 = fib_test(k - 1)
    k_2 = fib_test(k - 2)
    return k_1 + k_2


def fib_test(k):
    """求解第k个数的值"""
    # 没有递归终止条件
    return fib_test(k - 1) + fib_test(k - 2)


total = 0


def fib_test(k):
    """求解第k个数的值"""
    # 没有递归终止条件
    assert k > 0

    global total
    total += 1

    if k in [1, 2]:
        return 1
    return fib_test(k - 1) + fib_test(k - 2)


total = defaultdict(int)


def fib_test(k):
    """求解第k个数的值"""
    # 没有递归终止条件
    assert k > 0

    global total
    total[k] += 1

    if k in [1, 2]:
        return 1
    return fib_test(k - 1) + fib_test(k - 2)


def fib_test(k):
    """求解第k个数的值"""
    # 没有递归终止条件
    assert k > 0

    if k in [1, 2]:
        return 1
    return fib_test(k - 1) + fib_test(k - 2)


def fib_test2(k):
    """求解第k个数的值"""
    assert k > 0  # k 必须大于0
    # 没有递归终止条件
    if k in [1, 2]:
        return 1

    k_1 = 1
    k_2 = 1

    for i in range(3, k + 1):
        tmp = k_1
        k_1 = k_2 + k_1
        k_2 = tmp
    return k_1


def climb_stairs(s):
    """

    爬到最高层，每次只能爬一步或两步
    下一次的选择：走一步 + 走两步

    """
    # if s == 0:
    #     return
    if s == 1:
        return 1
    elif s == 2:
        return 2
    else:
        return climb_stairs(s-2) + climb_stairs(s-1)


def climb_stairs(s):
    """

    爬到最高层，每次只能爬一步或两步
    下一次的选择：走一步 + 走两步

    """
    # if s == 0:
    #     return
    if s in [0, 1]:  # 爬到第0级的方案数可看作1
        return 1

    else:
        return climb_stairs(s-2) + climb_stairs(s-1)


def fibonacci(n):
    if n in [1, 2]:
        return 2

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':

    # start = datetime.now()
    # fib_test(30)
    # print("递归耗时 {}s".format((datetime.now() - start).total_seconds()))

    # start = datetime.now()
    # fib_test(35)
    # print("递归耗时 {}s".format((datetime.now() - start).total_seconds()))
    # print(total)  # 运行次数

    # start = datetime.now()
    # fib_test2(30)
    # print("非递归耗时{}".format(datetime.now() - start))

    # start = datetime.now()
    # fib_test2(35)
    # print("循环耗时 {}s".format((datetime.now() - start).total_seconds()))
    # print(total)  # 运行次数
    pass

    # fib_test(4)

    # print(climb_stairs(3))

    while True:
        n = input("\n请输入月份！\n")
        if n == 'q':
            break

        print(fibonacci(int(n)))
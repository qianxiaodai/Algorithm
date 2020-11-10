# -*- coding: utf-8 -*-
import sys


def optimalLoad(weights, c):
    """

    :param weights: 货物重量
    :param c: 载货量
    :return:
    """
    tmp, ans = 0, 0  # 当前海盗船上的货物总重，货物数量
    weights.sort()
    for i in range(len(weights)):
        tmp += weights[i]
        if tmp <= c:
            ans += 1
        else:
            break
    return ans


def optimalLoad(weights, c):
    """

    :param weights: 货物重量
    :param c: 载货量
    :return:
    """
    tmp, ans = 0, n  # 当前海盗船上的货物总重，货物数量
    weights.sort()
    for i in range(len(weights)):
        tmp += weights[i]
        if tmp >= c:
            if tmp == c:
                ans = i + 1
            else:
                ans = i
    return ans


def main():
    print("请输入载重量c和古董数量n:")
    c, n = (int(x) for x in input().split())

    weights = []
    for idx, w in enumerate(sys.stdin):
        w = int(w.strip())
        weights.append(w)
        if idx == n - 1:
            break

    ans = optimalLoad(weights, c)
    return ans


if __name__ == '__main__':
    print("=" * 12 + "最优装载问题" + "=" * 12)
    res = main()
    print(res)

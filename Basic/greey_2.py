# -*- coding: utf-8 -*-
import sys
"""

物品可分割的装载问题称为背包问题。
物品不可分割的装载问题称为0-1背包问题。

"""


class Treasure:
    def __init__(self, w, v, p):
        self.w = w  # 宝物的重量
        self.v = v  # 宝物的价值
        self.p = p  # 宝物单位重量价值（性价比）

    @classmethod
    def parseFromInput(cls, w, v):
        return cls(w, v, v / w)


def getMaxValue(s, n):
    s = sorted(s, key=lambda x: x.p, reverse=True)
    profit = 0
    for i in range(len(s)):
        if s[i].w <= n:
            n -= s[i].w
            profit += s[i].v
        else:
            profit += s[i].p * n
            break
    return profit


def main():
    print("请输入宝物数量c和毛驴的承载能力n: ")
    c, n = (int(x) for x in input().split())
    s = [0 for _ in range(c)]
    for idx, line in enumerate(sys.stdin):
        w, v = (float(i) for i in line.strip().split())
        s[idx] = Treasure.parseFromInput(w, v)
        if idx == c - 1:
            break

    maxValue = getMaxValue(s, n)
    return maxValue


if __name__ == '__main__':
    res = main()
    print(res)



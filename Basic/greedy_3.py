# -*- coding: utf-8 -*-


import sys
# from functools import cmp_to_key
"""
高级钟点秘书：会议安排问题

"""


class Meet:

    def __init__(self, num, beg, end):
        self.num = num  # 记录会议的编号
        self.beg = beg  # 记录会议的开始时间
        self.end = end  # 记录会议的结束时间


class SetMeet:
    def __init__(self):
        self.n = int(input("请输入会议总数：\n"))
        self.m = [0 for _ in range(self.n)]
        print("请输入会议的开始时间和结束时间：")
        for idx, line in enumerate(sys.stdin):
            beg, end = (int(i) for i in line.strip().split())
            self.m[idx] = Meet(idx + 1, beg, end)

            if idx == self.n - 1:
                break

    def arrangeMeet(self):
        # 对会议按结束时间从小到大进行排序，若结束时间相同，按开始时间
        self.m = sorted(self.m, key=lambda x: (x.end, -x.beg))
        print("排完序的会议时间如下：")
        print("会议编号，开始时间， 结束时间")
        for i in range(self.n):
            print(f"{self.m[i].num :4d} {self.m[i].beg:8d} {self.m[i].end:10d}")

        print("=" * 30 + "=" * 30)
        print("选择会议的过程")
        print(f"  选择第{self.m[0].num}个会议")  # 选中了第一个会议
        ans = 1
        last = self.m[0].end

        for i in range(1, self.n):
            if self.m[i].beg >= last:
                ans += 1
                last = self.m[i].end
                print(f"  选择第{self.m[i].num}个会议")

        print(f"最多可安排{ans}个会议。")


def main():
    sm = SetMeet()
    sm.arrangeMeet()


# def cmp(x, y):
#     if x.end == y.end:
#         return x.beg > y.beg
#     else:
#         return x.end < y.end


# def cmp(x, y):
#     if x[2] == y[2]:
#         return x[1] > y[1]
#     else:
#         return x[2] < y[2]


if __name__ == '__main__':
    # a = [(1, 3, 6), (2, 1, 4), (3, 5, 7), (4, 2, 7)]
    # a = sorted(a, key=lambda x: (x[2], -x[1]))
    # print(a)

    # b = sorted(a, key=cmp_to_key(lambda x, y: cmp(x, y)))
    # print(b)

    main()
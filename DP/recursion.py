# -*- coding: utf-8 -*-


def to_str(n, base):
    if n < base:
        return str(n)
    else:
        return to_str(n//base, base) + str(n % base)


def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:  # 基线条件
        return convert_string[n]
    else:  # 递归终止条件
        return to_str(n//base, base) + convert_string[n % base]


def printN(n):
    if n:
        print(n)
        printN(n-1)


if __name__ == '__main__':
    # print(to_str(769, 10))
    printN(2)

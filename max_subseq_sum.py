# -*- coding: utf-8 -*-


def maxSubSum(seq, left, right):
    # maxLeftSum = 0
    # maxRightSum = 0
    leftBorderSum = 0
    rightBorderSum = 0
    maxLeftBorderSum = 0
    maxRightBorderSum = 0

    # 只有一个元素
    if left == right:
        return seq[left] if seq[left] > 0 else 0

    # 将数组一分为二
    center = (left + right) >> 1
    maxLeftSum = maxSubSum(seq, left, center)  # 递归求左边最大
    maxRightSum = maxSubSum(seq, center + 1, right)  # 递归求右边最大

    """求跨边界最大子列和"""
    # 从切分线开始往左扫描求左边最大和
    for i in range(center, left-1, -1):
        leftBorderSum += seq[i]
        if leftBorderSum > maxLeftBorderSum:
            maxLeftBorderSum = leftBorderSum

    # 从切分线开始往右扫描求右边最大和
    for i in range(center+1, right+1):
        rightBorderSum += seq[i]
        if rightBorderSum > maxRightBorderSum:
            maxRightBorderSum = rightBorderSum

    return max(maxLeftSum, maxRightSum, maxLeftBorderSum + maxRightBorderSum)


def maxSubSum1(seq):
    n = len(seq)
    this_sum, max_sum = 0, 0

    for i in range(n):
        this_sum += seq[i]  # 向右累加

        if this_sum > max_sum:
            max_sum = this_sum
        elif this_sum < 0:
            this_sum = 0
    return max_sum


if __name__ == '__main__':
    array = [4, -3, 5, -2, -1, 2, 6, -2]
    max_seq_sum = maxSubSum(array, 0, len(array)-1)
    print("\n", max_seq_sum)

    max_seq_sum = maxSubSum1(array)
    print("\n", max_seq_sum)

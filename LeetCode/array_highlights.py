# -*- coding: utf-8 -*-
# import re
from collections import Counter

"""

1. 删除数组中的重复项：
双指针：
i: 慢指针，存放要保留的数字
j: 快指针，找到要保留的数字
j找到与i位置不同的数，i后移一个位置
将j位置的数赋值给i位置的数。


2. 买卖股票的最佳时机（可再次购买）
找到连续的谷值和峰值，用峰值减去谷值。

3. 旋转数组
# https://leetcode-cn.com/problems/rotate-array/solution/xuan-zhuan-shu-zu-yuan-di-huan-wei-xiang-xi-tu-jie/
  注意：若旋转次数k=数组长度n, 则旋转后的数组变成原数组
 （1）暴力法
     旋转k次，每次将数组旋转1个元素

（2）使用额外的数组
     使用额外的数组把元素放到正确的位置上

（3）使用反转
     先反转所有元素，
     再反转前K个元素，
     再反转n-k个元素

4.两个数组的交集
交集中出现次数等于该数字在两个数组中出现次数的最小值
（1）哈希表
    （a）利用hash表统计较短数组中每个元素的出现次数。
    （b）遍历较长的数组，若当前元素在hash表中出现次数大于等于1，则将该元素添加到结果数组中，
        并减少hash表中该元素的出现次数。

（2）排序
    (1) 先对两个数组进行堆排
    (2) 用两个指针指向数组的头部，将指向较小数的指针向后移一位。
        若指针指向的数相等，则将该数添加到结果中，直至两个数组中有一个遍历完成为止。

5. 加一
    分两种情况，当前元素为9，当前元素不为9。
    倒序遍历数组
    （a）若当前元素为9，结果中当前元素为0
    （b）若当前元素不为9，结果中当前元素加一后返回。
    所以元素元素遍历完，说明高位全进位，数组长度加一，且第一位设为一。

6: 移动零
  将所有零移动到数组末尾，同时保持非0元素的相对顺序
  双指针：
  i:保存非0元素，
  j:找到非0元素，
  用nums[j]替换nums[i]或者nums[i]，nums[j]交换

6. 有效的数独
    判断9*9的数独是否有效
    1-9只在每一行出现一次
    1-9只在每一列出现一次
    1-9只在3*3宫格中出现一次
    方法：
        hash表
        （1）从上到下，从左到右遍历数组，判断 d = board[i][j]
            在第i行是否出现过， sets[(0, i, d)]
            在第j列是否出现过，sets[(1, j, d)]
            在第 z =（i // 3） * 3 + （j // 3）个box中是否出现过， set[(z, d)]
    遍历数独。
    检查看到每个单元格值是否已经在当前的行 / 列 / 子数独中出现过：
    如果出现重复，返回 false。
    如果没有，则保留此值以进行进一步跟踪。

7. 有效的字母异位词
给定字符串S和T, 判断S和T是否互为异位词。
（1）排序
（2）hash表（大小不固定的计数器）
 利用计数器计算S中每个字符出现的次数，
 利用T减少计数器中每个字符出现的次数。
 遍历计数器，若当前字符的出现次数不为0，则说明S和T不为变为词，否则为变位词。
 
 8. 判断是否为回文串
    方法一：筛选  + 遍历
        对字符串s进行一次遍历，并将其中的字母和数字进行保留，放在另一个字符串中sgood中。
        然后判断sgood是否是回文串即可。
        判断方法有两种：
        （a） 利用字符串的反转函数，判断反转后的字符串与原字符串是否相等。
        （b） 利用双指针
            左右指针分别指向sgood的两侧，两个指针相向移动
            每移动一步，判断这两个指针指向的元素是否相等。
            当两个指针相遇，说明是回文串。
    
    方法二：在原字符串上直接判断
        （a）初始时，左右指针分别指向原字符串的两侧，
        （b）左指针向右移动，找到第一个字母或数字
         (b) 右指针向左移动，找到第一个字母或数字
        （c）判断左右指针指向元素是否相等：
              若不相等，则不为回文串
              否则，重复步骤（b）- （c）直至两指针相遇，则为回文串。

8. 字符串转换成整数
 （1）处理空格
 （2）处理正负号
 （3）提取数字，提取数字的过程中，判断数字是否溢出

"""
import collections


class Solution:
    def removeDuplicates(self, nums: list)->int:
        """
        1. 删除数组中的重复项
        remove duplicate items
        """
        if not nums:  # 如果数组为空
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1

    def maxProfit(self, prices: list)->int:
        """

        2. 买卖股票的最佳时机
        best time to buy and sell stock

        """
        if not prices:
            return 0

        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]

        return max_profit

    # def maxProfit(self, prices: list)->int:
    #     """在斜坡上不断爬升，持续增加连续交易获取的利润"""
    #     if not prices:
    #         return 0
    #
    #     max_profit = 0
    #
    #     i = 0
    #     while i < len(prices) - 1:
    #         # 遍历股价，找到第一个谷值
    #         while i < len(prices) - 1 and prices[i] >= prices[i+1]:
    #             i += 1
    #         vally = prices[i]
    #
    #         # 遍历股价，找到第一个峰值
    #         while i < len(prices) - 1 and prices[i] <= prices[i+1]:
    #             i += 1
    #         peak = prices[i]
    #
    #         max_profit += (peak - vally)
    #
    #     return max_profit

    # 超时
    def rotate(self, nums: list, k: int)->int:
        """递归解决数组旋转，k控制递归深度"""
        if k:
            n = len(nums)
            tmp = nums[-1]
            for i in range(n-2, -1, -1):
                nums[i+1] = nums[i]
            nums[0] = tmp
            self.rotate(nums, k-1)

        return nums

    def rotate(self, nums: list, k: int)->None:
        n = len(nums)
        k = k % n
        while k:
            previous = nums[-1]  # previous存放替换的数字
            for i in range(n):
                tmp = nums[i]  # tmp存放被替换的数字
                nums[i] = previous
                previous = tmp
            k -= 1

    def rotate(self, nums: list, k: int)->None:
        """使用额外的数组"""
        n = len(nums)
        res = [0] * n

        for i in range(n):
            res[(i + k) % n] = nums[i]
        nums[:] = res

    def rotate(self, nums: list, k: int)->None:
        """使用反转"""
        n = len(nums)
        k = k % n

        nums[:] = nums[::-1]
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

    def rotate(self, nums: list, k: int)->None:
        """使用反转"""
        n = len(nums)
        k = k % n
        self.reversed(nums, 0, n-1)
        self.reversed(nums, 0, k-1)
        self.reversed(nums, k, n-1)

    def reversed(self, nums, l, r):
        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l += 1
            r -= 1

    def intersect(self, nums1: list, nums2: list) -> list:
        if not nums1 or not nums2:
            return []

        nums1.sort()  # 就地排序
        nums2.sort()  # 就地排序

        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1

            else:
                res.append(nums1[i])
                i += 1
                j += 1

        return res

    def intersect(self, nums1: list, nums2: list) -> list:

        if len(nums1) > len(nums2):  # nums1为两个数组中较短的数组
            nums1, nums2 = nums2, nums1

        res = []
        hash_table = {}

        for item in nums1:
            hash_table[item] = hash_table.get(item, 0) + 1

        for item in nums2:  # 按键取值
            if item in hash_table and hash_table[item]:
                res.append(item)
                hash_table[item] -= 1
        return res

    def intersect(self, nums1: list, nums2: list) -> list:

        num1 = collections.Counter(nums1)
        num2 = collections.Counter(nums2)
        num = num1 & num2
        return num.elements()

    def plusOne(self, digits: list) -> list:
        """

        :param digits:
        :return:
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        digits[0:0] = [1]
        return digits

    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        for j in range(len(nums)):
            if nums[j] != 0:
                i += 1
                if j > i:
                    nums[i], nums[j] = nums[j], nums[i]

    def isValidSudoku(self, board: list) -> bool:
        sets = {}

        for i in range(9):
            for j in range(9):
                d = board[i][j]
                if d == '.':
                    continue
                z = (j // 3) + (i // 3) * 3
                if (z, d) in sets or (0, i, d) in sets or (1, j, d) in sets:
                    return False
                sets[(z, d)] = 1
                sets[(0, i, d)] = 1  # 行
                sets[(1, j, d)] = 1  # 列

        return True

    def isValidSudoku(self, board: list) -> bool:

        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        box = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                val = ord(board[i][j]) - ord('1')
                if row[i][val] != 0 or col[j][val] != 0 or box[j // 3 + (i // 3) * 3][val] != 0:
                    return False
                row[i][val], col[j][val], box[j // 3 + (i // 3) * 3][val] = 1, 1, 1
        return True

    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start = 0
        gap = len(matrix) - 1

        while gap > 0:
            for i in range(gap):
                matrix[start][start + i], matrix[start + i][start + gap], \
                    matrix[start + gap][start + gap - i], matrix[start + gap - i][start] = \
                    matrix[start + gap - i][start], matrix[start][start + i], \
                    matrix[start + i][start + gap], matrix[start + gap][start + gap - i]

            gap -= 2
            start += 1

    def reverse(self, x: int) -> int:

        MAX_VALUE = 2147483647 if x > 0 else 2147483648

        ans, y = 0, abs(x)

        while y:

            pop = y % 10
            ans = ans * 10 + pop  # 注意顺序

            if ans > MAX_VALUE:
                return 0
            y = y // 10

        return ans if x > 0 else -ans

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}
        for i in range(len(s)):
            counter[s[i]] = counter.get(s[i], 0) + 1
            counter[t[i]] = counter.get(t[i], 0) - 1

        for c in counter():
            if counter.get(c) != 0:
                return False

        return True

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True

        s = s.lower()
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True

    def myAtoi(self, s: str) ->int:
        i, n = 0, len(s)

        while i < n and s[i] == ' ':  # 找到第一个非空白字符
            i += 1

        # 若第一个字符不是数字也不是正负号，则为无效字符
        # 若该字符串为空格串，则为无效串
        if i == n or (not s[i].isdigit() and s[i] not in ['+', '-']):
            return 0

        # 判断正负性：
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1

        elif s[i] == '+':
            i += 1

        boundary = (1 << 31) - 1 if sign == 1 else (1 << 31)
        ans = 0  # 提取数字
        while i < n and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            if ans > boundary:
                return sign * boundary
            i += 1

        return sign * ans

    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0

        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1

            else:
                i = i - j + 1
                j = 0

        if j == len(needle):
            return i - j
        else:
            return -1

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        seq = self.countAndSay(n - 1)
        i, s = 0, ''
        while i < len(seq):
            cnt = 1
            while i < len(seq) - 1 and seq[i] == seq[i + 1]:
                cnt += 1
                i += 1

            s += str(cnt)
            s += seq[i]
            i += 1
        return s

    def countAndSay(self, n: int) -> str:

        pre_num = '1'

        for i in range(1, n):
            next_num, cnt, cur_num = '', 1, pre_num[0]
            for j in range(1, len(pre_num)):
                if pre_num[j] == cur_num:
                    cnt += 1
                else:
                    next_num += str(cnt) + cur_num
                    cur_num = pre_num[j]
                    cnt = 1
        next_num += str(cnt) + cur_num
        pre_num = next_num
        return pre_num

    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_copy = nums1[:m]

        i, j = 0, 0
        k = 0
        while i < m and j < n:
            if nums1_copy[i] <= nums2[j]:
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        if i < m:
            nums1[k:] = nums1_copy[i:m]

        if j < n:
            nums1[k:] = nums2[j:n]

    def removeElement(self, nums: list, target: int) -> int:
        """删除数组中指定元素"""
        i = 0

        for j in range(len(nums)):
            if nums[j] != target:
                if i != j:
                    nums[i] = nums[j]
                i += 1
        return i

    def threeSum(self, nums: list)->list:
        n = len(nums)
        nums.sort()
        ans = list()
        for first in range(n):
            # 需要和上次枚举的数不同
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            '''错误的去重'''
            # if nums[first] == nums[first + 1]:
            #     continue

            # 对应的指针初值指向数组的最右端
            third = n - 1
            target = -nums[first]

            for second in range(first + 1, n):
                # 需要和上一次枚举的数不同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                while second < third and nums[second] + nums[third] > target:
                    third -= 1

                if second == third:
                    break

                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans

    def minSubArrayLen(self, s: int, nums: list) -> int:
        """实现长度最小的子数组"""
        n = len(nums)
        minLen = float('inf')

        for i in range(n):  # 设置子序列起点i
            seqSum = 0

            for j in range(i, n):  # 设置子序列终点j
                seqSum += nums[j]
                if seqSum >= s:  # 一旦子序列和不小于s, 更新minLen
                    seqLen = j - i + 1  # 取子序列长度
                    if minLen > seqLen:
                        minLen = seqLen
                        break  # 跳出当前循环，进入下一轮循环

        return 0 if minLen == float("inf") else minLen
        # return 0 if i == n else minLen  # i 是局部变量

    def minSubArrayLen(self, s: int, nums: list) -> int:
        """实现长度最小的子数组"""
        n = len(nums)
        minLen = float('inf')
        seqSum = 0

        i = 0  # 设置子序列起点i

        for j in range(n):  # 设置子序列终点j
            seqSum += nums[j]
            while seqSum >= s:  # 根据当前子序列和的情况，不断调节子序列的起始位置
                seqLen = j - i + 1  # 取子序列长度
                if minLen > seqLen:
                    minLen = seqLen
                seqSum -= nums[i]
                i += 1
        return 0 if minLen == float("inf") else minLen

    def spiralOrder(self, matrix: list) -> list:
        if not matrix or not matrix[0]:
            return []
        n, m = len(matrix), len(matrix[0])
        # num, tar = 1, n *
        l, r, t, b = 0, m - 1, 0, n - 1
        mat = []

        while True:
            for i in range(l, r + 1):
                mat.append(matrix[t][i])
                # num += 1
            t += 1

            if t > b:
                break

            for i in range(t, b + 1):
                mat.append(matrix[i][r])
                # num += 1

            r -= 1

            if l > r:
                break

            for i in range(r, l - 1, -1):
                mat.append(matrix[b][i])
                # num += 1
            b -= 1

            if t > b:
                break

            for i in range(b, t - 1, -1):
                mat.append(matrix[i][l])
                # num += 1
            l += 1

            if l > r:
                break

        return mat

    def generateMatrix(self, n: int) -> list:
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1):  # left to right
                mat[t][i] = num
                num += 1
            t += 1

            if t > b:
                break

            for i in range(t, b + 1):  # top to bottom
                mat[i][r] = num
                num += 1
            r -= 1

            if l > r:
                break

            for i in range(r, l - 1, -1):  # right to left
                mat[b][i] = num
                num += 1
            b -= 1

            if t > b:
                break

            for i in range(b, t - 1, -1):  # bottom to top
                mat[i][l] = num
                num += 1
            l += 1

            if l > r:
                break

        return mat

    def wordPattern(self, pattern: str, s: str) -> bool:
        if not str and not s:
            return True

        h = {}
        pattern = list(pattern)
        s = s.split()

        if len(pattern) != len(s):
            return False
        for p, s in zip(pattern, s):
            if p in h:
                if h[p] != s:
                    return False
                else:
                    continue
            else:
                if s in h.values():
                    return False

                else:
                    h[p] = s

        return True


if __name__ == '__main__':
    obj = Solution()
    # obj.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    # print(obj.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    # print(obj.maxProfit([1, 7, 2, 3, 6, 7, 6, 7]))
    # print(obj.maxProfit([1, 7, 2, 3, 6, 7, 6, 7]))
    # digits = [1, 2, 3, 4, 5, 6, 7]
    # obj.rotate(digits, 3)
    # print(digits)
    # print(obj.intersect([9, 4, 9, 8, 4], [4, 9, 5]))
    # print(obj.plusOne([1, 2, 9]))
    # print(obj.rotate([[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]))
    # print(obj.reverse(123))

    # print(obj.reverse(1534236469))
    # print(obj.isAnagram("anagram", "nagaram"))

    # print(obj.isPalindrome("A man, a plan, a canal: Panama"))

    # print(obj.strStr("hello", "ll"))

    # print(obj.countAndSay(4))

    # print(obj.threeSum([-1, 0, 1, 2, -1, -4]))
    # print(obj.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    # print(obj.minSubArrayLen(11, [1, 2, 3, 4, 5]))
    # print(obj.spiralOrder([[2, 5, 8], [4, 0, -1]]))
    print(obj.generateMatrix(4))
    # print(obj.generateMatrix(3))

    # "abba"
    # "dog cat cat fish"
    print(obj.wordPattern("abba", "dog cat cat fish"))


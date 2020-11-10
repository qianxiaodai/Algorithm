# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/merge-intervals/solution/he-bing-qu-jian-by-leetcode-solution/
"""


class Solution:

    def pivot_index(self, nums: list) ->int:
        if len(nums) < 3:
            return -1
        s = sum(nums)
        leftsum = 0

        for i, num in enumerate(nums):
            if leftsum == s - num - leftsum and i <= len(nums) - 2:
                return i
            leftsum += num
        return -1

    def search_insert(self, nums: list, target: int) -> int:
        """
        前提：数组有序
        找到第一个比目标值大的数， 返回插入位置
        找到第一个与目标值相等的数，返回其索引
        没有找到大于等于目标值的数, 则插入到尾部
        :param nums:
        :param target:
        :return:
        """
        for i, num in enumerate(nums):
            if target <= num:
                return i
        else:  # 没有找到大于等于目标值的数, 则插入到尾部
            return len(nums)

    def search_insert(self, nums: list, target: int) -> int:
        """
        前提：数组有序
        找到第一个比目标值大的数， 返回插入位置
        找到第一个与目标值相等的数，返回其索引
        没有找到大于等于目标值的数, 则插入到尾部
        :param nums:
        :param target:
        :return:
        """
        left, right = 0, len(nums) - 1
        ans = len(nums)
        while left <= right:
            mid = (left + right) >> 1
            if target <= nums[mid]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def merge(self, intervals):
        sorted_arr = sorted(intervals, key=lambda x: x[0])
        merged = []
        for interval in sorted_arr:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], intervals[1])
        return merged

    def twosum(self, nums, target):
        """
        遍历每个x, 并查找数组中是否存在与target-x相等的值。
        """
        # m, n = -1, -1
        for i, x in enumerate(nums):
            for j in range(i+1, len(nums)):
                if target - x == nums[j]:
                    return [i, j]
        return None

    def twosum(self, nums, target):
        d = {}
        n = len(nums)
        for x in range(n):
            if target - nums[x] in d:
                return [d[target - nums[x]], x]
            else:
                d[nums[x]] = x

    def reverse(self, x):
        y, res = abs(x), 0
        # 32位整数数值范围为 [−2^31,  2^31 − 1]
        # python运算符优先级，先乘除后加减，位运算符低于算术运算符，移位运算符高于按位运算符
        boundary = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            pop = y % 10
            res = res * 10 + pop
            if res > boundary:
                return 0
            y //= 10
        return res if x > 0 else -res

    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        res = 0

        while x > res:
            res = res * 10 + x % 10
            x //= 10

        return x == res or x == res // 10
    
    def removeElement(self, nums, target):
        """就地删除数组中所有等于target的值"""
        for n in nums[:]:
            if n == target:
                nums.remove(n)
        return len(nums)

    def removeElement(self, nums, val):
        """就地删除数组中所有等于target的值"""
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        # print(nums)
        return i

    def removeDuplicates(self, nums: list) -> int:

        nums[:] = list(sorted(set(nums)))
        return len(nums)

    def removeDuplicates(self, nums: list) -> int:

        # i = 0
        # for j in range(1, len(nums)):
        #     if nums[i] != nums[j]:
        #         i += 1
        #         nums[i] = nums[j]
        # return i + 1

        i, j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]

        return i + 1

    def romanToInt(self, s: str) -> int:
        """
        1. 建立一个hashMap来映射符号和值
        2. 遍历字符串，若当前字符串的值小于右边，则减去当前值
           否则加上当前值。
        :param s:
        :return:
        """
        roman_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        res = 0
        for j in range(1, len(s)):
            if roman_int[s[i]] >= roman_int[s[j]]:
                res += roman_int[s[i]]
                i += 1
            else:
                res -= roman_int[s[i]]
                i += 1
        # print(s[i])
        res += roman_int[s[i]]
        return res

    def countAndSay(self, n: int) -> str:
        pre_str = "1"
        for j in range(1, n):
            # 初始化下一个字符串，上一个字符串的第一个字符，计数器
            next_str, cur_char, count = '', pre_str[0], 1
            for i in range(1, len(pre_str)):
                """
                遍历上一个字符串
                若当前字符串与cur_char相等，计数器加1，
                否则，将count和cur_char追加到next_str中
                cur_char更新为cur_char，count置为1，重新计数。
                下一个字符串更新上一个字符串
                重复此步骤，直到达到迭代次数为止
                """
                if cur_char == pre_str[i]:
                    count += 1
                else:
                    next_str += str(count) + cur_char
                    cur_char = pre_str[i]
                    count = 1
            next_str += str(count) + cur_char
            pre_str = next_str
        return pre_str

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        brackets = []

        symbols = {'(': ')', '[': ']', '{': '}'}  # 利用hash表
        for char in s:
            if char in '([{':  # 碰到左边括号入栈
                brackets.append(char)  # 入栈
            elif char in ')]}':  # 碰到右边括号
                if not brackets:  # 若栈为空，说明没有足够多的右括号与左括号匹配
                    return False
                top = brackets.pop()  # 栈定元素出栈
                if char != symbols[top]:  # 判断括号类型是否匹配正确
                    return False
        return brackets == []   # 若栈为空，则匹配正确，否则没有足够的左括号与右括号匹配

    def isValid(self, s: str)-> bool:  # 是否是有效的括号
        brackets = []
        for char in s:
            if char == '(':
                brackets.append(')')
            elif char == '[':
                brackets.append(']')
            elif char == '{':
                brackets.append('}')
            elif not brackets:
                return False
            else:
                top = brackets.pop()
                if top != char:
                    return False
        return brackets == []

    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1

        carry = 0  # 进位
        ans = ""
        while i >= 0 and j >= 0:
            sum = int(a[i]) + int(b[j]) + carry
            carry = sum // 2
            sum %= 2
            ans += str(sum)
            i -= 1
            j -= 1

        while i >= 0:
            sum = int(a[i]) + carry
            carry = sum // 2
            sum %= 2
            ans += str(sum)
            i -= 1

        while j >= 0:
            sum = int(b[j]) + carry
            carry = sum // 2
            sum %= 2
            ans += str(sum)
            j -= 1

        if carry:
            ans += str(carry)

        return ans


if __name__ == '__main__':
    obj = Solution()
    # print(obj.pivot_index([-1, -1, 0, 1, 1, 0]))
    # print(obj.pivot_index([1, 2, 3]))
    # print(obj.pivot_index([-1, -1, -1, -1, -1, 0]))
    # print(obj.pivot_index([1, 7, 3, 6, 5, 6]))
    # print(obj.search_insert([1, 3, 5, 6], 0))
    # print(obj.search_insert([1, 3, 5, 6], 7))
    # print(obj.search_insert([1, 3, 5, 6], 1))
    # print(obj.search_insert([1, 3, 5, 6], 6))

    # print(obj.merge([[1, 6], [8, 10], [15, 18]]))
    # print(obj.twosum([3, 3], 6))
    # print(obj.reverse(-123))
    # print(obj.isPalindrome(123321))
    # print(obj.removeDuplicates([1, 1, 2]))

    # print(obj.removeElement([1, 1, 2], 1))
    # print(obj.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
    # print(obj.romanToInt("LVIII"))

    # a = [1, 2, 3]
    # print(id(a))
    # a.remove(1)
    # print(id(a))
    # print(obj.countAndSay(4))
    print(obj.addBinary("11", "1"))
    pass

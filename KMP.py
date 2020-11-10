# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/implement-strstr/solution/shi-xian-strstr-by-leetcode/
# https://www.bilibili.com/video/BV1PA411h7VY?from=search&seid=14718233780334117886

from collections import Counter

"""
问题一:
找出模式串在目标串中第一次出现的开始位置

问题二:
给定

找出模式串在目标串中所有的出现起始位置
"""

"""

文本匹配算法
基于滑动窗口的解法
(1) 子串逐一比较法/ 枚举法
缺点：将目标串中的所有子串与模式串进行比较。

(2) 字符逐一比较/ 双指针法
只有模式串的第一个字符
与目标串中滑动窗口的
第一个字符相等时才需要
比较，一旦不匹配，开始回溯
j = 0 / j归0
i = j - i + 1 / i 回到上一次匹配位置的下一个位置

缺点：
低效， 因为要发生回溯

(3) KMP算法
在暴力匹配的基础之上引入了前缀与后缀，
将模式串通过前缀后缀初始化next数组。
在文本串去匹配模式串的时候，
使用next数组，某个字符失配时，
该字符对应的next值会告诉你下一步匹配中，
模式串应该跳到哪个位置，
从而简化了指针的回溯，以达到优化的目的。

"""


class Solution:

    def match(self, haystack: str, needle: str)->int:
        """
        沿着字符串逐一移动滑动窗口, 将滑动窗口中的字符与
        模式串进行逐一比较
        """
        l, n = len(needle), len(haystack)

        for start in range(n - l + 1):  # 滑动窗口移动次数
            if haystack[start: start+l] == needle:
                return start

        return -1

    def match(self, haystack: str, needle: str) -> int:
        """双指针法"""
        i, j = 0, 0
        m, n = len(haystack), len(needle)

        # if m == 0 and n == 0:
        #     return 0
        #
        # elif m != 0 and n == 0:
        #     return 0

        if n == 0:
            return 0

        while i < m and j < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:  # 回溯
                i = i - j + 1
                j = 0

        if j == n:
            return i - j
        return -1

    def match(self, haystack: str, needle: str)->int:
        L, n = len(needle), len(haystack)
        if L == 0:
            return 0

        pn = 0
        while pn < n - L + 1:
            # find the position of the first needle character
            # in the haystack string
            while pn < n - L + 1 and haystack[pn] != needle[0]:
                pn += 1

            # compute the max match string
            curr_len = pL = 0
            while pL < L and pn < n and haystack[pn] == needle[pL]:
                pn += 1
                pL += 1
                curr_len += 1

            # if the whole needle string is found,
            # return its start position
            if curr_len == L:
                return pn - L

            # otherwise, backtrack
            pn = pn - curr_len + 1

        return -1

    def KMPSearch(self, pat, txt):
        """

        :param pat:
        :param txt:
        :return:
        """
        M = len(pat)  # 文本串长度
        N = len(txt)  # 模式串长度

        lps = [0] * M  # lps数组保存模式串中最长相等前后缀
        j = 0

        self.computeLPSArray(pat, M, lps)

        i = 0

        while i < N:
            if j == M - 1:
                print("Found pattern at index " + str(i-j))
                j = lps[j-1]

            if pat[j] == txt[i]:
                i += 1
                j += 1

            elif pat[j] != txt[i]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1

    # Python program for KMP Algorithm
    def KMPSearch(self, pat, txt):
        M = len(pat)
        N = len(txt)

        # create lps[] that will hold the longest prefix suffix
        # values for pattern
        lps = [0] * M
        j = 0  # index for pat[]

        # Preprocess the pattern (calculate lps[] array)
        self.computeLPSArray(pat, M, lps)

        i = 0  # index for txt[]
        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1

            if j == M:
                print("Found pattern at index " + str(i - j))
                j = lps[j - 1]

            # mismatch after j matches
            elif i < N and pat[j] != txt[i]:
                # Do not match lps[0..lps[j-1]] characters,
                # they will match anyway
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

    def computeLPSArray(self, pat, M, lps):
        len = 0

        i = 1

        while i < M:
            if pat[len] == pat[i]:  # 前缀的前缀与后缀的后缀相等时
                len += 1  # 前缀后移
                lps[i] = len  # 前缀和后缀的最大匹配长度加1
                i += 1  # 后缀后移

            else:  # 前缀和后缀不等
                if len != 0:  # 一直找前缀的前缀，直到前缀的前缀与后缀的后缀相等
                    len = lps[len-1]

                else:
                    lps[i] = 0
                    i += 1

        print("lps:", lps)


if __name__ == '__main__':
    obj = Solution()
    # print(obj.match("mississippi", "a"))

    text = "AABAACAADAABAABA"
    pattern = "AABA"
    obj.KMPSearch(pattern, text)
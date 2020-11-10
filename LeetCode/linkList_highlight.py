# -*- coding: utf-8 -*-
"""
2. 回文链表
1）：利用快慢指针找到链表的中点，反转后半部分链表，再比较
慢指针走一步，快指针走两步。
快指针到达链表尾部时，慢指针走到链表的中间。
（慢指针走的步数是快指针的一半）

2): 将链表值复制到数组中，将问题转化为判断数组是否为回文数组。
判断数组是否为回文数组。
a) 用双指针法
b) 排序法

3）利用字符串链表转整数的思想（很慢）
从前往后得到的数字和从后往前得到的数字一样。

3. 删除链表中倒数第n个结点
1） 删除链表中倒数第n个结点，就是删除链表从头开始数的第L-n+1个结点，其中L为链表长度。
    a) 两次遍历
    i) 第一次遍历找到链表长度L
    ii)第二次遍历找到第L-n个结点，将第L-n个结点的Next指针指向L-n+1的Next，
        即可完成第L-n+l个结点的删除。

4. 判断环形链表
1）利用hash表思想
   遍历所有结点，每次遍历一个结点（不是结点值）时，判断该结点是否被访问过。
2）利用快慢指针
    快指针走一步，慢指针走两步。
    初始时，慢指针在head位置，快指针在head.next。
    在移动过程中，快指针反过来追上慢指针，则说明链表为环形链表。
    否则指针到达尾部，链表不为环形链表。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """头插法建表的思想/双指针"""
        pre = ListNode(None)  # 定义一个头结点
        cur = head  # cur结点用于提取结点

        while cur:
            nextTmp = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = nextTmp
        return cur

    def add(self, head, node):
        new_node = ListNode(node)
        if not head:
            head = new_node
            return head
        else:
            r = head
            while r.next:
                r = r.next

            r.next = new_node
            return head

    def reverseList(self, head: ListNode) -> ListNode:
        """链表反转"""
        if not head or not head.next:
            return head

        pre = self.reverseList(head.next)  # 当前结点的子节点都已反转完毕

        # 反转当前结点
        # head.next 指向pre尾结点， head结点插入pre尾部
        head.next.next = head
        head.next = None
        return pre  # 返回已反转链表的头结点

    def isPalindrome(self, head: ListNode) -> bool:
        """2. 回文链表"""

        h, t = 0, 0
        base = 1
        cur = head
        while cur:
            h = h * 10 + cur.val
            t = base * cur.val + t
            base *= 10
            cur = cur.next
        return h == t

    def isPalindrome(self, head: ListNode) -> bool:
        """2. 回文链表"""

        if not head or not head.next:  # 如果链表为空或者只有
            return True

        fast, slow = head, head

        while fast.next and fast.next.next:  # slow指向链表的中点
            fast = head.next.next
            slow = slow.next

        slow = self.reversedList(slow.next)  # 将链表右半部分反转

        while slow:  # 利用双指针判断是否是回文链表
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next

        return True

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """3. 删除链表中倒数第n个结点(链表中至少有一个结点)"""
        dummy = ListNode(None)  # 定义一个哑结点
        dummy.next = head

        first = head
        L = 0

        while first:
            """第一次遍历找到链表长度L"""
            first = first.next
            L += 1

        length = L - n
        first = dummy
        while length:
            """第二次遍历找到第L-n个结点"""
            first = first.next
            length -= 1

        first.next = first.next.next

        return dummy.next

    def hasCycle(self, head: ListNode) -> bool:
        """4. 判断环形链表"""
        sets = {}

        while head:
            if head in sets:  # 不是将结点值加入hash表中
                return True

            else:
                sets[head] = ''

            head = head.next

        return False

    def hasCycle(self, head: ListNode) -> bool:
        """4. 判断环形链表"""
        sets = {}

        while head:
            if head in sets:  # 不是将结点值加入hash表中
                return True

            else:
                sets[head] = ''

            head = head.next

        return False

    def hasCycle(self, head: ListNode) -> bool:
        """4. 判断环形链表"""
        slow, fast = head, head.next

        while fast != slow:
            if not fast or not fast.next: # 说明到达链表尾部
                return False

            fast = fast.next.next
            slow = slow.next

        return True

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        pre, p = dummy, head

        while p:
            if pre.val == p.val:
                tmp = p
                pre.next = tmp.next
                p = tmp.next
                del tmp
            else:
                pre = p
                p = p.next
        return dummy.next

    def deleteDuplicates(self, head: ListNode) -> ListNode:

        p = head

        while p and p.next:  # 链表中至少有两个节点
            if pre.val == p.val:
                tmp = p
                pre.next = tmp.next
                p = tmp.next
                del tmp
            else:
                pre = p
                p = p.next
        return p


if __name__ == '__main__':
    obj = Solution()
    # obj.reverseList(pre)
    # p = obj.add(None, 1)
    # p = obj.add(p, 2)
    # p = obj.add(p, 3)
    # obj.reverseList(p)
    # obj.isPalindrome(p)
    # obj.hasCycle(None)







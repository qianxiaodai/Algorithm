# -*- coding: utf-8 -*-
from copy import deepcopy

"""

使用队列模拟栈
方法一：使用两个队列
队列1保存栈中元素，队列2作为入栈操作的辅助队列
元素先入队列2， 若队列1不为空，将队列1中的元素依次出队入队列2
将队列2与队列1互换。

方法二：使用1个队列
先将新元素入队，然后，将新元素之前的所有元素依次出队并入队，
此时队列的前端为新入栈的栈顶元素。


"""


class Solution:
    def generateMatrix(self, n):
        res = [[0] * n for _ in range(n)]  # 定义一个二维数组

        startx, starty = 0, 0  # 定义每一圈的起始位置
        loop = n // 2  # 循环圈数，n = 3, 循环一圈，矩阵中间的值需要单独处理
        mid = n // 2  # 矩阵中间元素位置，n为3， 中间的位置就是(1，1)，n为5，中间位置为(2, 2)

        count = 1  # 用来给矩阵中每一个空格赋值
        offset = 1  # 每一圈循环，需要控制每一条边遍历的长度

        while loop:
            i = startx
            j = starty

            # 下面开始的四个while就是模拟转了一圈

            # 模拟填充上行从左到右(左闭右开)
            while j < starty + n - offset:
                res[startx][j] = count
                j += 1
                count += 1

            # 模拟填充右列从上到下(左闭右开)
            while i < startx + n - offset:
                res[i][j] = count
                i += 1
                count += 1

            # 模拟填充下行从右到左(左闭右开)
            while j > starty:
                res[i][j] = count
                j -= 1
                count += 1

            # 模拟填充左列从下到上(左闭右开)
            while i > startx:
                res[i][j] = count
                i -= 1
                count += 1

            startx += 1
            starty += 1

            offset += 2

            loop -= 1

        if n % 2:
            res[mid][mid] = count

        return res


class LinkNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self, head=None):
        """
        Initialize your data structure here.
        """
        self.head = LinkNode(None)
        if head:
            self.head.next = head
        self.size = 0

    def __str__(self):
        ans = []

        flag = 0
        cur = self.head.next
        while cur:
            if not flag:
                flag = 1
            else:
                ans.append(' -> ')
            ans.append(str(cur.val))
            cur = cur.next

        return f"{''.join(ans)}"

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size or index < 0:
            return -1

        cur = self.head.next

        while index:
            cur = cur.next
            index -= 1

        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = LinkNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        cur = self.head
        while cur.next:
            cur = cur.next

        new_node = LinkNode(val)

        cur.next = new_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list,
        the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """

        if index > self.L:
            return

        cur = self.head

        while index > 0:
            cur = cur.next
            index -= 1

        new_node = LinkNode(val)
        new_node.next = cur.next
        cur.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        cur = self.head
        while index:
            cur = cur.next
            index -= 1

        tmp = cur.next
        cur.next = tmp.next
        del tmp
        self.size -= 1

    # def reverseList(self, head: LinkNode) -> LinkNode:
    #     if not head or not head.next:
    #         return head
    #
    #     pre = self.reverseList(head.next)  # 当前结点的子节点都已反转完毕
    #
    #     # 反转当前结点
    #     # head.next 指向pre尾结点， head结点插入pre尾部
    #     head.next.next = head
    #     head.next = None
    #     return pre  # 返回已反转链表的头结点

    def reverseList(self, head: LinkNode) -> LinkNode:
        #    pre = None
        #    cur = head
        return MyLinkedList(self.reverse(None, head))

        # return self.head

    def reverse(self, pre, cur):
        if cur is None:
            return pre

        tmp = cur.next
        cur.next = pre

        return self.reverse(cur, tmp)


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue2.append(x)

        while self.queue1:
            # print(self.queue1)
            val = self.queue1.pop(0)
            self.queue2.append(val)

        '''
        有问题
        self.queue1 = self.queue2
        self.queue2.clear()
        '''
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return

        return self.queue1.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return

        return self.queue1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return

        return self.queue.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return

        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue


if __name__ == '__main__':
    obj = Solution()
    ans = obj.generateMatrix(3)
    myLink = MyLinkedList()
    # myLink.deleteAtIndex(0)
    # print(myLink)
    # print(myLink.get(1))
    # myLink.addAtHead(1)
    # myLink.deleteAtIndex(0)
    # print(myLink)

    # myLink.addAtHead(1)
    # myLink.deleteAtIndex(0)
    # print(myLink)
    # myLink.addAtTail(4)
    # myLink.addAtTail(3)
    # print(myLink.get(0))
    # print(myLink.get(1))
    # print(myLink.get(2))
    # print(myLink)
    myLink.addAtTail(1)
    myLink.addAtTail(2)
    # myLink.addAtTail(3)
    # print(myLink)
    otherLink = deepcopy(myLink)
    reversedLink = myLink.reverseList(otherLink.head.next)
    # print(reversedLink)
    # print(myLink)

    s = MyStack()
    s.push(1)
    s.push(2)
    # s.push(3)
    # print(s.queue)




# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, None, None)

    # def helper(self, root: TreeNode, lower, upper) -> bool:
    #     if not root:
    #         return True
    #
    #     val = root.val
    #
    #     # if lower and val : Error
    #     if lower is not None and val <= lower:
    #         return False
    #
    #     if upper is not None and val >= upper:
    #         return False
    #
    #     return self.helper(root.left, lower, val) and self.helper(root.right, val, upper)

    def sortedArrayToBST(self, nums: list) -> TreeNode:
        return self.helper(nums, 0, len(nums) - 1)

    # def helper(self, nums: object, left: object, right: object) -> object:
    #     if left > right:
    #         return None
    #
    #     mid = left + (right - left) // 2
    #
    #     root = TreeNode(nums[mid])
    #
    #     root.left = self.helper(nums, left, mid - 1)
    #     root.right = self.helper(nums, mid + 1, right)
    #
    #     return root

    def binaryTreePaths(self, root: TreeNode) -> list:
        res, path = [], ''
        return self.dfs(res, path, root)

    def dfs(self, res, path, root):
        pass

    # def preorderTraversal(self, root: TreeNode) -> list:
    #     res = []
    #     if root:
    #         res.append(root.val)
    #         res[len(res):] = self.preorderTraversal(root.left)
    #         res[len(res):] = self.preorderTraversal(root.right)
    #
    #     return res
    def preorderTraversal(self, root: TreeNode) -> list:
        res = []
        if root:
            res.append(root.val)
            res[len(res):] = self.preorderTraversal(root.left)
            res[len(res):] = self.preorderTraversal(root.right)

        return res


if __name__ == '__main__':
    obj = Solution()
    # obj.sortedArrayToBST([-10, -3, 0, 5, 9])

    from collections import deque
    root = TreeNode(1)

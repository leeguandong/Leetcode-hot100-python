"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。
"""

# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/solutions/131121/dong-hua-yan-shi-si-chong-jie-fa-114-er-cha-shu-zh
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        queue = []

        def dfs(root):
            if not root:
                return
            queue.append(root)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        head = queue.pop(0)
        head.left = None
        while queue:
            tmp = queue.pop(0)
            tmp.left = None
            head.right = tmp
            head = tmp

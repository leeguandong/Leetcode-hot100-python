"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。
"""

from typing import Optional


# https://leetcode.cn/problems/symmetric-tree/solutions/2015063/ru-he-ling-huo-yun-yong-di-gui-lai-kan-s-6dq5

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.treeSame(root.left, root.right)

    def treeSame(self, p, q):
        if p is None or q is None:
            return p is q

        return p.val == q.val and self.treeSame(p.left, q.right) and self.treeSame(p.right, q.left)

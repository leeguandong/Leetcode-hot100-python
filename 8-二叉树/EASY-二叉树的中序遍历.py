"""
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
"""

#
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def order(self, root, res):
        if root == None:
            return
        self.order(root.left, res)
        res.append(root.val)
        self.order(root.right, res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.order(root, res)
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    result = Solution().inorderTraversal(root)
    print(result)

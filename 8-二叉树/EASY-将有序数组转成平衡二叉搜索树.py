"""
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡二叉搜索树。
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/solutions/313814/yi-wen-du-dong-shi-yao-shi-er-cha-sou-suo-shu-bst-
# 题解就一句话，中间拉起来，两边递归成树
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def makeTree(start, end):
            if start > end:
                return

            mid = (start + end) // 2
            midTree = TreeNode(nums[mid])
            midTree.left = makeTree(start, mid - 1)
            midTree.right = makeTree(mid + 1, end)
            return midTree

        return makeTree(0, len(nums) - 1)

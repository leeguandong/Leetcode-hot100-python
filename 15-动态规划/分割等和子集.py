"""
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。
"""
from typing import List
from functools import cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # @cache
        # def dfs(i,c):
        #     if i<0:
        #         return c==0
        #     return c>=nums[i] and dfs(i-1,c-nums[i]) or dfs(i-i,c)

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> bool:
            if i < 0:
                return j == 0
            return j >= nums[i] and dfs(i - 1, j - nums[i]) or dfs(i - 1, j)

        s = sum(nums)
        return s % 2 == 0 and dfs(len(nums) - 1, s // 2)


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    print("\n")
    print(Solution().canPartition(nums))

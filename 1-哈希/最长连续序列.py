"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
"""


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0  # 记录最长连续序列的长度
        num_set = set(nums)  # 记录nums中的所有数值
        for num in num_set:
            # 如果当前的数是一个连续序列的起点，统计这个连续序列的长度
            if (num - 1) not in num_set:
                seq_len = 1  # 连续序列的长度，初始为1
                while (num + 1) in num_set:
                    seq_len += 1
                    num += 1  # 不断查找连续序列，直到num的下一个数不存在于数组中
                res = max(res, seq_len)  # 更新最长连续序列长度
        return res


if __name__ == "__main__":
    Solution().longestConsecutive([100, 4, 200, 1, 3, 2])

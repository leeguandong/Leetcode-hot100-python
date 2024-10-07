"""
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

示例 1：
输入：nums = [1,2,0]
输出：3
解释：范围 [1,2] 中的数字都在数组中。

示例 2：
输入：nums = [3,4,-1,1]
输出：2
解释：1 在数组中，但 2 没有。

示例 3：
输入：nums = [7,8,9,11,12]
输出：1
解释：最小的正数 1 没有出现。
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for a in nums:  # 遍历每个座位，记当前坐着a号乘客
            while 0 < a <= len(nums) and a != nums[a - 1]:  # 乘客a是正票但坐错了! 其座位被 ta=nums[a-1]占了
                nums[a - 1], a = a, nums[a - 1]  # a和ta两人互换则a对号入座。此后ta相当于新的a，去找自己的座位（循环执行）

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1  # 找到首个没有对号入座的nums[i]!=i+1
        return len(nums) + 1  # 满座，返回N+1


if __name__ == "__main__":
    Solution().firstMissingPositive([1, 2, 0])

"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

"""
from typing import List


# https://www.bilibili.com/video/BV1Xj411K7oF/?vd_source=4aed82e35f26bb600bc5b46e65e25c22

class Solution:
    def rob(self, nums: List[int]) -> int:
        cur, pre = 0, 0

        for num in nums:
            cur, pre = max(pre + num, cur), cur

        return cur


if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    print(Solution().rob(nums))


# 打家劫舍算法题的状态转移方程：dp[i] = max(dp[i-2] + nums[i], dp[i-1])
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#
#         dp = [0] * len(nums)
#         dp[0] = nums[0]
#
#         for i in range(1, len(nums)):
#             dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
#
#         return dp[-1]

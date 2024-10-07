"""
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
必须在不使用库内置的 sort 函数的情况下解决这个问题。

示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]

"""


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        left, point, right = 0, 0, len(nums) - 1
        while point <= right:
            if nums[point] == 2:
                nums[right], nums[point] = nums[point], nums[right]
                right -= 1
                continue
            if nums[point] == 0:
                nums[left], nums[point] = nums[point], nums[left]
                left += 1
            point += 1


# 链接：https://leetcode.cn/problems/sort-colors/solutions/672825/75-yan-se-fen-lei-pythonzhi-zhen-yi-bian-0vct/

if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    print(Solution().sortColors(nums))

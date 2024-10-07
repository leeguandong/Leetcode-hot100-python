"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
"""
from typing import List


# https://leetcode.cn/problems/set-matrix-zeroes/solutions/2461030/xian-gai-xing-hou-gai-lie-ga-ga-by-rin-o-0g60
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_pos = []  # 记录改列位置
        for ind, row in enumerate(matrix):
            for idx, val in enumerate(row):
                if val == 0:
                    zero_pos.append(idx)
                    matrix[ind] = [0] * len(row)  # 先改行
                else:
                    continue
        for pos in set(zero_pos):
            for row in range(len(matrix)):
                matrix[row][pos] = 0  # 后改列


if __name__ == "__main__":
    Solution().setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

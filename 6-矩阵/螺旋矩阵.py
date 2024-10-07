"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""
from typing import List


# https://leetcode.cn/problems/spiral-matrix/solutions/2057738/python-zip-by-zhuzhzzz-tk7a
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result += matrix.pop(0)  # 取矩阵第一行并删除
            matrix = list(zip(*matrix))[::-1]  # 旋转矩阵
        return result


if __name__ == "__main__":
    Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

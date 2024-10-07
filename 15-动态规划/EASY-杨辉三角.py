"""
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        c = [[1] * (i + 1) for i in range(numRows)]

        for i in range(2, numRows):
            for j in range(1, i):
                c[i][j] = c[i - 1][j - 1] + c[i - 1][j]

        return c


if __name__ == '__main__':
    print(Solution().generate(5))

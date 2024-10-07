"""
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        col = [0] * n

        def valid(r, c):
            for R in range(r):
                C = col[R]
                if R + C == r + c or R - C == r - c:
                    return False
            return True

        def dfs(r, s):
            if r == n:
                ans.append(["." * c + "Q" + "." * (n - c - 1) for c in col])
                return

            for c in s:
                if valid(r, c):
                    col[r] = c
                    dfs(r + 1, s - {c})

        dfs(0, set(range(n)))
        return ans


if __name__ == '__main__':
    print(Solution().solveNQueens(4))

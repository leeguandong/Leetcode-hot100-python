"""
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例 1：
输入：n = 12
输出：3
解释：12 = 4 + 4 + 4

示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9

"""
from cmath import inf
from functools import cache
from math import isqrt


@cache
def dfs(i, j):
    if i == 0:
        return inf if j else 0

    if j < i * i:
        return dfs(i - 1, j)
    return min(dfs(i - 1, j), dfs(i, j - i * i) + 1)


class Solution:
    def numSquares(self, n: int) -> int:
        return dfs(isqrt(n), n)


if __name__ == '__main__':
    n = 12
    print(Solution().numSquares(n))

# 状态转移方程：dp[i] = min(dp[i], dp[i - j * j] + 1)

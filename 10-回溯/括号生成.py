"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]

"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = 2 * n
        path = [""] * m
        ans = []

        def dfs(i, left):
            if i == m:
                ans.append("".join(path.copy()))
                return

            if left < n:
                path[i] = "("
                dfs(i + 1, left + 1)
            if i - left < left:
                path[i] = ")"
                dfs(i + 1, left)

        dfs(0, 0)
        return ans


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))

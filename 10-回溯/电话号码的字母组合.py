"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""
from typing import List

MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        path = [""] * n
        ans = []
        if n == 0:
            return []

        def dfs(i):
            if i == n:
                ans.append("".join(path.copy()))
                return

            for x in MAPPING[int(digits[i])]:
                path[i] = x
                dfs(i + 1)

        dfs(0)
        return ans

if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
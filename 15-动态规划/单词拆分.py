"""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""
from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        @cache
        def dfs(i):
            if i == n:
                return True
            for j in range(i + 1, n + 1):
                if s[i:j] in wordDict and dfs(j):
                    return True
            return False

        return dfs(0)


# https://leetcode.cn/problems/word-break/solutions/2916680/shi-pin-jiao-ni-yi-bu-bu-si-kao-dong-tai-zcw7/

if __name__ == "__main__":
    print(Solution().wordBreak("leetcode", ["leet", "code"]))

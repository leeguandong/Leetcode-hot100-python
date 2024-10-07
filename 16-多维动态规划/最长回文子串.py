"""
给你一个字符串 s，找到 s 中最长的
回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"

"""



# class Solution(object):
#     def longestPalindrome(self, s):
#         res = ''
#         for i in range(len(s)):
#             start = max(i - len(res) -1, 0)
#             temp = s[start: i+1]
#             if temp == temp[::-1]:
#                 res = temp
#             else:
#                 temp = temp[1:]
#                 if temp == temp[::-1]:
#                     res = temp
#         return res


# 链接：https://leetcode.cn/problems/longest-palindromic-substring/solutions/1601761/by-yu-chen-gg-kz5y/


class Solution:
    def longestPalindrome(self, s: str) -> str:

        size = len(s)
        # 特殊处理
        if size == 1:
            return s
        # 创建动态规划dynamic programing表
        dp = [[False for _ in range(size)] for _ in range(size)]
        # 初始长度为1，这样万一不存在回文，就返回第一个值（初始条件设置的时候一定要考虑输出）
        max_len = 1
        start = 0
        for j in range(1, size):
            for i in range(j):
                # 边界条件：
                # 只要头尾相等（s[i]==s[j]）就能返回True
                if j - i <= 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        cur = j - i + 1
                # 状态转移方程
                # 当前dp[i][j]状态：头尾相等（s[i]==s[j]）
                # 过去dp[i][j]状态：去掉头尾之后还是一个回文（dp[i+1][j-1] is True）
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        cur_len = j - i + 1
                # 出现回文更新输出
                if dp[i][j]:
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i

        return s[start:start + max_len]



# 链接：https: // leetcode.cn / problems / longest - palindromic - substring / solutions / 662473 / 5 - zui - chang - hui - wen - zi - chuan - dong - tai - gu - p7uk /

if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))
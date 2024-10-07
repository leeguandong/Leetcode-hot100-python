"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号
子串的长度。

示例 1：
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

示例 2：
输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"

示例 3：
输入：s = ""
输出：0
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        res = 0
        for i in range(len(s)):
            if not stack or s[i] == '(' or s[stack[-1]] == ')':
                stack.append(i)
            else:
                stack.pop()
                res = max(res, i - (stack[-1] if stack else - 1))
        return res


# https://leetcode.cn/problems/longest-valid-parentheses/solutions/762279/32-zui-chang-you-xiao-gua-hao-fu-zhu-zha-1cqq/


if __name__ == "__main__":
    print(Solution().longestValidParentheses("(()"))

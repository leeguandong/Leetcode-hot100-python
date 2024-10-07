"""
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例 1：
输入：s = "3[a]2[bc]"
输出："aaabcbc"

示例 2：
输入：s = "3[a2[c]]"
输出："accaccacc"

示例 3：
输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"

示例 4：
输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
"""

# https://leetcode.cn/problems/decode-string/solutions/19447/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/?envType=study-plan-v2&envId=top-100-liked

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        multi = 0

        for c in s:
            if c == "[":
                stack.append([multi, res])
                multi = 0
                res = ""
            elif c == "]":
                last_multi, last_res = stack.pop()
                res = last_res + last_multi * res
            elif "0 " <= c <= "9":
                multi = multi * 10 + int(c)
            else:
                res += c

        return res

if __name__ == '__main__':
    s = "3[a]2[bc]"
    print(Solution().decodeString(s))

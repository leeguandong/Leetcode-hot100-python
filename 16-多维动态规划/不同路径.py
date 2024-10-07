"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 初始化为１，避免多余的赋值，外层不使用*，否则浅拷贝内层可能会在赋值时候出现问题
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1]


# https: // leetcode.cn / problems / unique - paths / solutions / 55536 / dong - tai - gui - hua - duo - yu - yan - by - wf0312 /

if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))

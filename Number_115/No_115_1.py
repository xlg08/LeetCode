class Solution:

    def numDistinct(self, s: str, t: str) -> int:

        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        #t,j 作列   s,i 作行

        # 初始化第一行和第一列
        for i in range(len(s)):
            dp[i][0] = 1
        for j in range(1, len(t)):
            dp[0][j] = 0

        # 将 s 字符串中的每个元素都对t字符串进行一次扫描
        for i in range(1, len(s)+1):    #外层循环：s  行  i

            for j in range(1, len(t)+1):    #内层循环：t  列   j

                if s[i-1] == t[j-1]:        # i 行       j 列

                    #dp[i][j]：  s[0 .. i-1] 的子序列中等于 t[0..j-1] 的数量。
                    # dp[i-1][j-1] 为 dp[i][j]   的左上角元素
                    # dp[i-1][j]   为 dp[i][j]   的正上方元素
                    # 如果当前字符相同，则将 左上角数量加正上方数量，赋给该位置
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    # 如果当前字符不同，则将 正上方数量，赋给该位置
                    dp[i][j] = dp[i-1][j]


        return dp[-1][-1]

if __name__ == '__main__':
    so = Solution()
    s = "rabbbit"
    t = "rabbit"
    print(so.numDistinct(s, t))

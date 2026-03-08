from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        n = len(s)  # 桌子长度

        # 1. 构建前缀和数组 preSum，用于快速计算任意区间内的盘子总数
        preSum, sum = [0] * n, 0  # 前缀和数组(表示从开头到位置 i 有多少个盘子('*'))， 累积的盘子数量

        # 左侧最近的蜡烛位置 left
        left, l = [0] * n, -1           # 左侧最近蜡烛位置，
        for i, ch in enumerate(s):      # 遍历桌子数组
            if ch == '*':
                sum += 1
            else:
                l = i
            preSum[i] = sum
            left[i] = l

        # 右侧最近的蜡烛位置 right
        right, r = [0] * n, -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                r = i
            right[i] = r

        # 处理查询
        ans = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            x, y = right[x], left[y]
            if x >= 0 and y >= 0 and x < y:
                ans[i] = preSum[y] - preSum[x]

        return ans


if __name__ == '__main__':

    s = "**|**|***|"
    queries = [[2, 5], [5, 9]]
    so = Solution()
    print(so.platesBetweenCandles(s, queries))

    s = "***|**|*****|**||**|*"
    queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
    print(so.platesBetweenCandles(s, queries))

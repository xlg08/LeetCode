class Solution:
    def findContentChildren(self, g, s) -> int:

        g.sort()
        s.sort()

        # 变量 index_g 和 index_s 分别指向 g、s 初始位置
        index_g, index_s = 0, 0
        res = 0         # 使用res保存结果  ->   满足孩子数

        while index_g < len(g) and index_s < len(s):
            if g[index_g] <= s[index_s]:            # 孩子的胃口数 <= 饼干尺寸
                res += 1
                index_g += 1
                index_s += 1
            else:
                index_s += 1        # 饼干数

        return res


if __name__ == '__main__':
    g = [2, 2]      # 孩子胃口
    s = [1, 1, 1]       # 饼干尺寸

    so = Solution()
    print(so.findContentChildren(g, s))

    g = [1, 2]
    s = [1, 2, 3]

    print(so.findContentChildren(g, s))



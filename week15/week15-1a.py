# week15-1a.py 學習計畫 DP - Multidimensional P1
# Leetcode 62. Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def f(i,j):
            if i==m-1 and j==n-1: return 1#走到終點,回傳一種路徑
            if i==m or j==n: return 0#走到邊界
            return f(i+1,j)+f(i,j+1)#往下 往右
        return f(0,0)
        
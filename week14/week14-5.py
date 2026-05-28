# week14-5.py 學習計畫 1D DP P4
# leetcode 790. Domino and Tromino Tiling
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9+7
        @cache
        def f(n):
            if n==0:return 1
            if n==1:return 1
            if n==2:return 2
            ans = f(n-1) + f(n-2)
            #L型
            for i in range(3, n+1):
                ans = (ans + f(n-i) * 2)%MOD
            return ans
        return f(n) 
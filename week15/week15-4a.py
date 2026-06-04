# week15-4a.py 學習計畫 DP - Multidimensional P4
# Leetcode 72. Edit Distance
# 插入 刪掉 更換 字母幾次會跟word2相同
# Top-Down函式呼叫
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        @cache
        def f(i,j):
            if i==M and j==N:return 0#走到底了
            if i==M:return N-j#word2剩下的,都刪掉
            if j==N:return M-i#word1剩下的,都刪掉
            if word1[i]==word2[j]:return f(i+1,j+1)#已經一樣了
            #ans1 = f(i+1, j)
            #ans2 = f(i, j+1)
            #ans3 = f(i+1, j+1)
            return min(f(i+1, j), f(i, j+1), f(i+1, j+1)) + 1
        return f(0, 0)


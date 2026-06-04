# week15-2b.py 學習計畫 DP - Multidimensional P2
# Leetcode 1143. Longest Common Subsequence
# 建表用bottom-up DP
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        t = [ [0] *(N+1) for i in range(M+1)]
        for i in range(M):
            for j in range(N):
                if text1[i] == text2[j]: t[i+1][j+1] = t[i][j] + 1#相同看左上+1
                t[i+1][j+1] = max(t[i+1][j+1], t[i+1][j], t[i][j+1])#不相同,找當下 左邊 上面 誰大
        return t[M][N]
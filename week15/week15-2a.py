# week15-2a.py 學習計畫 DP - Multidimensional P2
# Leetcode 1143. Longest Common Subsequence
# Top-Down函式呼叫
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        @cache
        def f(i,j):
            if i==M or j==N: return 0
            if text1[i] == text2[j]: return 1 + f(i+1,j+1)#下一位
            else: return max(f(i,j+1),f(i+1,j))#不同時，取左邊或上面誰大
        return f(0,0)
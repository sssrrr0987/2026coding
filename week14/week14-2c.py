# week14-2c.py 學習計畫 1D DP P1
# leetcode 1137. N-th Tribonacci Number
class Solution:
    @cache #函式呼叫函式(不重複問答案)
    def tribonacci(self, n: int) -> int:
        a = [0, 1, 1]
        if n<3 :return a[n] 
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

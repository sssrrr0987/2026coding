# week14-4.py 學習計畫 1D DP P3
# leetcode 198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache #遇到DP,就用top-down DP來思考
        def f(i): #如果搶到第i間房,最後能拿到多少錢
            if i >= len(nums):return 0 #整條街走完,沒得搶
            return nums[i] + max(f(i+2),f(i+3))
            
        return max(f(0), f(1))
        
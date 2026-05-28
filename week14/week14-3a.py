# week14-3a.py 學習計畫 1D DP P2
# leetcode 746. Min Cost Climbing Stairs
# 找出最少成本,每次階梯能走1階或2階
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache #來自from functools import *
        def helper(i):
            if i>=len(cost):return 0
            return cost[i] + min(helper(i+1), helper(i+2))
        return min(helper(0), helper(1))
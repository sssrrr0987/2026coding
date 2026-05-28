# week14-3b.py 學習計畫 1D DP P2
# leetcode 746. Min Cost Climbing Stairs
# 找出最少成本,每次階梯能走1階或2階
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        a = [0] * (N+1)
        a[0] = cost[0]
        a[1] = cost[1]
        for i in range(2, N+1):
            a[i] = min(a[i-1], a[i-2])
            if i<N: a[i] += cost[i]
        return a[N]
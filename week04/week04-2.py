# =week04-2.py 學習計畫 prefix sum P1
# leetcode 1732. Find the Highest Altitude
# 找到最高的海拔高度,所以一直加
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = H = 0
        n = len(gain)
        for i in range(n):
            H += gain[i]
            ans = max(ans, H)
        return ans
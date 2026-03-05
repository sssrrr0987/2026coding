#week02-4.py 學習計畫 two pointers P3
#leetcode 11. Container With Most Water
#找出裝最多水的面積.使用雙指標找出最高的牆，不是最高的牆其指標就移動
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j =0, len(height)-1 #左右指標
        ans = 0
        while i<j:
            area = (j-i) * min(height[i], height[j])
            ans = max(ans, area)#更新當下最大的面積
            if height[i] < height[j]: i+=1#不是最高的牆其指標就移動
            else: j-=1
        return ans

        
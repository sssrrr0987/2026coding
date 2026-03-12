# week03-5.py 學習計畫sliding window P4
# 1493. Longest Subarray of 1's After Deleting One Element
#一定要刪一值,找出最多1的字串
#想成一個區間內能容忍一個0
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        zeros = 0
        tail = 0
        n= len(nums)
        for head in range(n):
            if nums[head] == 0:zeros += 1#計算剩餘次數
            while zeros > 1:#把次數調回正常
                if nums[tail] == 0:zeros -= 1
                tail += 1
            ans = max(ans, head-tail+1)
        return ans - 1 #前面算到的值是最長,還沒刪
        
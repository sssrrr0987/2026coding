# week03-2.py 學習計畫sliding window P1
# 643. Maximum Average Subarray I
# 控制框大小,逐步+尾-頭 毛毛蟲法!?
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        total = sum(nums[:k])#計算框總和
        ans = total
        for i in range(k,n):#逐步找最大的框
            total = total + nums[i] - nums[i-k]
            ans = max(ans, total)
        return ans / k

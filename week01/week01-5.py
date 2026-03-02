# week01-5.py 學習計畫 Array/String P7
# leetcode 238. Product of Array Except Self
# 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        presum = [1]
        postsum = [1]
        N=len(nums)
        for i in range(N):
            presum.append(presum[-1]*nums[i])#左開始乘的前綴和
            postsum.append(postsum[-1]*nums[N-i-1])#右開始乘的前綴和
        ans = []
        for i in range(N):
            ans.append(presum[i]*postsum[N-i-1])
        return ans
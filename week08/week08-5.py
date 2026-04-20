# week08-5.py 學習計畫 Binary Search P3
# leetcode 162. Find Peak Element
# 找到比左右鄰居大的值,回傳它index
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:return 0

        for  i in range(N):
            if i == 0:
                if nums[i] > nums[i+1]:return i#左邊界時
            elif i == N-1:
                if nums[i] > nums[i-1]:return i#右邊界時
            elif nums[i] > nums[i-1] and nums[i] >nums[i+1]:return i
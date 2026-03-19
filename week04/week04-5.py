# week04-5.py 學習計畫 prefix sum P2
# leetcode 724. Find Pivot Index
# 找出中間index使左右總和相等
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + nums[i])
        postfix = [0] * (n+1)
        for i in range(n-1, -1, -1):
            postfix[i] = postfix[i+1] + nums[i]
        print(prefix)
        print(postfix)
        for i in range(n):#先從第一格開始不算,比對其左右總和是否一樣
            if prefix[i] == postfix[i+1]:return i#左總和跟右總和差一格
        return -1
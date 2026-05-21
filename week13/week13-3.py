# week13-3.py 學習計畫 Heap/Priority Queue P1
# leetcode 215. Kth Largest Element in an Array
# 不用sort找第幾大的值
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #作弊法
        # nums.sort()
        # return nums[-k]

        #要用Heap資料結構,可找出最小的數
        # heapify(nums)#變heap資料結構
        # while nums:
        #     print(heappop(nums))

        #最後版本
        heapify(nums)#logN
        for i in range(len(nums)-k):#吐掉不用N-k個數
            heappop(nums)
        return heappop(nums)
        
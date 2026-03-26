# week05-2c.py 學習計畫 Hash Table(Map/Set)
# 2215. Find the Difference of Two Arrays
# 輸出左右各自沒有的數
# 很慢版本->2版->3版
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 ,nums2 = set(nums1), set(nums2)#先將重複值刪掉 2版
        return [list(nums1 - nums2), list(nums2 - nums1)]#set相減 3版
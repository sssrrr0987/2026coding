# week05-2a.py 學習計畫 Hash Table(Map/Set)
# 2215. Find the Difference of Two Arrays
# 輸出左右各自沒有的數
# 很慢版本
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1, ans2 = [], []
        for i in nums1:#看當前值是否於另一個list中
            if i not in nums2:
                ans1.append(i)
        for i in nums2:
            if i not in nums1:
                ans2.append(i)
        return [list(set(ans1)), list(set(ans2))]#list轉set 再轉2維list
# week01-4.py 學習計畫 Array/String P3
# leetcode 1431. Kids With the Greatest Number of Candies
#輸出list中的值加上額外的數,是否為該list值中的最大值
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        M = max(candies)
        ans = []
        for i in candies:
            if i+extraCandies >= M: ans.append(True)
            else: ans.append(False)
        return ans
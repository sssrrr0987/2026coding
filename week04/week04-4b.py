# week04-4b.py(week04-3.py) 學習計畫 prefix sum 
# leetcode 3866. First Unique Even Element
# 找到list中 第一個 只有出現一次的偶數是誰
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        n = len(nums)
        H = [0] * 200# 表 H[??] 對應 ??出現幾次
        for i in nums:
            H[i] += 1
        for i in nums:
            if i % 2 == 0 and H[i] == 1:  return i
        return -1

#     def firstUniqueEven(self, nums: list[int]) -> int:
#         n = len(nums)
#         H = [0] * 200# 表 H[??] 對應 ??出現幾次
#         for i in range(n):
#             H[nums[i]] += 1
#         for i in range(n):
#             if nums[i] % 2 == 0 and H[nums[i]] == 1:
#                 return nums[i]
#         return -1

        
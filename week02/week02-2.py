#week02-2.py 學習計畫 two pointers P1
# leetcode 283. Move Zeroes
#將非0數移至左邊
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = 0
        for i in range(n):#先將非0數移至k這個指標
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for i in range(k,n):#剩下位置補0
            nums[i] = 0
        
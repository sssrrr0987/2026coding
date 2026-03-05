#week02-5.py 學習計畫 two pointers P4
#leetcode 1679. Max Number of K-Sum Pairs
#輸出一個數列中,最多有幾組 數組pair 數相加後的值為k
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        i, j = 0, len(nums)-1

        while i<j:
            if nums[i]+nums[j] == k:
                ans+=1
                i+=1
                j-=1
            elif nums[i]+nums[j] < k:#小於k讓左指標變大
                i+=1
            else: j-=1#大於k讓右指標變小
            

        return ans
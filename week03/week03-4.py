# week03-4.py 學習計畫sliding window P3
# 1004. Max Consecutive Ones III
#找出最長的 連續1的字串,並有更改k次0->1的機會
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        zeros = 0
        tail = 0#尾巴目前位置
        ans = 0
        for head in range (n):
            if nums[head] == 0:#目前是0的化,消耗一次變化機會
                zeros += 1

                while zeros >k:#開始吐,把變化機會調回區間
                    if nums[tail] == 0:
                        zeros -= 1 #補回次數
                    tail += 1 #尾巴位置右移
            ans = max(ans, head-tail+1)
        return ans

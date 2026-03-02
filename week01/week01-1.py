#week01-1.py (LeetCode挑戰題)
#leetcode 1401. Number of Steps to Reduce a Number in Binary Representation to One
#把二進位的字串, 模擬「偶數除2、奇數加1」問幾步後會變成1。
class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        n = int(s,2)#2進制轉10進制
        while n !=1:
            if(n%2==0):n=n//2
            else: n=n+1
            ans+=1
        return ans
        
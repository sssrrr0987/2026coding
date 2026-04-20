# week08-6.py 學習計畫 Binary Search P4
# leetcode 875. Koko Eating Bananas
# 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #準備函式helper(ans)來看答案對不對
        def helper(k): #1小時吃k個,能於h小時內吃完嗎
            total = 0
            for pile in piles:
                total += pile // k
                if pile % k > 0:total += 1
            return total <= h #回傳是否符合條件
        return bisect_left(range(1,max(piles)), True, key=helper)+1
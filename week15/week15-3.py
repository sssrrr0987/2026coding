# week15-3.py 學習計畫 DP - Multidimensional P3
# Leetcode 714. Best Time to Buy and Sell Stock with Transaction Fee
# Top-Down函式呼叫
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def f(i, hasStack):#目前價錢時,有股票嗎    
            if i == len(prices): return 0
            #手上有股票,要不要賣
            if hasStack:ans = prices[i] + f(i+1, False) - fee#今天賣,進入明天
            #手上沒股票,要不要買
            else:ans = -prices[i] + f(i+1,True)#今天買進入明天
            #不買不賣
            return max(ans, f(i+1,hasStack))

        return f(0, False)
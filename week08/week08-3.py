# week08-3.py 學習計畫 Binary Search P1
# 374. Guess Number Higher or Lower
# 呼叫guess()找1-n中的站
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #for i in range(n+1):print(-guess(i), end=' ')
        return bisect_left(range(n+1), 0, key=lambda x:-guess(x))
        

        # for i in range(1, n+1):#暴力法太慢,n到20億
        #     if guess(i) == 0:return i
        
        # left, right = 1, n+1#左包含 右包含
        # while left < right:
        #     mid = (left + right) // 2
        #     if guess(mid)  == 0:return mid#猜中了
        #     if guess(mid) > 0:left = mid + 1#再猜高一點了
        #     else:right = mid#再猜低一點
        # return left
    
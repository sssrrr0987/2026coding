#week02-3.py 學習計畫 P2
#leetcode 392. Is Subsequence
#一層迴圈，裡面同時有兩個變數index變數，叫two pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        n1 ,n2 = len(s), len(t)
        i = 0
        if n1 == 0:return True #坑,左邊空字串,就不用比了
        for k in range(n2):
            if s[i] == t[k]: i+=1#左右序列相同,將左指標+1
            if i == n1:return True#左指標跑完,就結束判斷
        
        return False
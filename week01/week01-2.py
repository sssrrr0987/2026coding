#week01-2.py 學習計畫 Array/String P1
#leetcode 1768. Merge Strings Alternately
#陣列互相插植
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        len1, len2 = 0,0 
        while len1<len(word1) or len2<len(word2):
            if len1 < len(word1):
                ans += word1[len1]
                len1 += 1
            if len2 < len(word2):
                ans += word2[len2]
                len2 += 1
        
        return ans

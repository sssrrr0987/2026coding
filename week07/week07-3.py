# week07-3.py 學習計畫 Stack P1
# leetcode 2390. Removing Stars From a String
# 遇到*刪掉前一項字元
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i == '*':stack.pop()
            else :stack.append(i)
        return ''.join(stack)#用'空格'.join()把陣列轉字串
        
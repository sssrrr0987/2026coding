# week07-4.py 學習計畫 Stack P3
# leetcode 394. Decode String
# 重複數字後的字串
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        nowN, nowS = 0, ''#存數字, 存字串
        for c in s:
            if c.isdigit():#存數字.10進位組合處理
                nowN = nowN *10 + int(c)
            elif c.isalpha():#是字母
                nowS += c
            elif c == '[':
                stack.append( (nowN, nowS) )
                nowN, nowS = 0, ''
            elif c == ']':
                prevN, prevS = stack.pop()
                nowS = prevS + prevN * nowS#舊的字串 加上需重複的字串
        return nowS
# week03-3.py 學習計畫sliding window P2
# 1456. Maximum Number of Vowels in a Substring of Given Length
# 長度k的眶中最多有多少母音
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        count = 0
        for i in range(k):
            if s[i] in vowels: count += 1#先暫存第一個框內有多少值
        ans = count
        n = len(s)
        for i in range(k, n):
            if s[i] in vowels: count += 1#尾巴是母音先加
            if s[i-k] in vowels: count -= 1#頭是母音再減
            ans = max(ans, count)
        return ans
        
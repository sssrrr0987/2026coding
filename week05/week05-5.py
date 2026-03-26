# week05-5.py 學習計畫 Hash Table(Map/Set) P3
# 1657. Determine if Two Strings Are Close
# 看能否使左右字串 移動位置後相等
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        if counter1 == counter2:return True #值跟數量 完全相同
        if sorted(counter1.values()) == sorted(counter2.values()): return True #數量相同,因為能轉換其值
        return False
        
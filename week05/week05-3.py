# week05-3.py 學習計畫 Hash Table(Map/Set) P2
# 1207. Unique Number of Occurrences
# 每種數字出現的次數需不同
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr) #統計次數
        s = set() #存出現次數
        for i in counter:
            if counter[i] in s:return False #有出現過出事
            s.add(counter[i]) #沒有出現過,就存set中
        return True
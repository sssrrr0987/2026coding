# week05-6.py 學習計畫 Hash Table(Map/Set) P4
# 2352. Equal Row and Column Pairs
# row 跟col有幾組相同
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = Counter()
        ans = 0
        for row in grid:
            counter[ tuple(row) ] += 1
        #tuple() 把陣列[3,1,2,2] 變不會動 (3,1,2,2)
        #因為Hash Map 的key只能放不會動的
        for col in zip(*grid):
            ans += counter[ tuple(col) ]
        return ans
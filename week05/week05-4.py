# week05-4.py 2026-03-25每日題
# 3546. Equal Sum Grid Partition I
# 切一刀 兩邊總和是否相同
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum( [sum(row) for row in grid]) #

        presum = 0
        for row in grid:
            presum += sum(row)
            if presum == total - presum: return True #上半 等於 下半

        presum = 0
        for col in zip(*grid):#轉置矩陣
            presum += sum(col)  
            if presum == total - presum: return True
        return False
        
        # *grid *會把2維list拉直 row(123)row(123)row(123)
        # zip() 會轉置矩陣 新的矩陣成為 row 1 1 1
        #                             row 2 2 2
        #                             row 3 3 3

        

        
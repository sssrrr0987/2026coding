# week13-2.py 學習計畫 graph - BFS P2
# leetcode 994. Rotting Oranges
# 看幾天橘子爛光
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        queue = deque() #佇列
        visited = set()
        fresh = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    visited.add( (i, j) )
                    queue.append( (i, j, 0) )
                if grid[i][j] == 1:fresh += 1#多1個新鮮橘子
        if fresh == 0:return 0#特例
        ans = -1
        
        while queue:
            i ,j, step = queue.popleft()#先進先出,取座標與步數
            ans = step
            for ii, jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):#走右左上下
                if ii<0 or jj<0 or ii >= M or jj >= N:continue#檢查邊界
                if (ii, jj) in visited:continue

                if grid[ii][jj] == 1:#能感染
                    fresh -= 1
                    visited.add( (ii, jj) )
                    queue.append( (ii, jj, step+1) )
        if fresh>0:return -1#還有新鮮就不是全爛
        return ans

        
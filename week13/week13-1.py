# week13-1.py 學習計畫 graph - BFS P1
# leetcode 1926. Nearest Exit from Entrance in Maze
# 找最短出口要幾步
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        M, N = len(maze), len(maze[0])
        queue = deque() #佇列
        queue.append( (entrance[0], entrance[1], 0) ) #先走起點 (i,j,目前第幾步)
        visited = set()
        visited.add(tuple(entrance))#list轉tuple

        while queue:
            i ,j, step = queue.popleft()#先進先出,取座標與步數
            for ii, jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):#走右左上下
                if ii<0 or jj<0 or ii >= M or jj >= N:continue#檢查邊界
                if maze[ii][jj] == '+':continue#撞牆

                if (ii, jj) not in visited:#檢查走過沒
                    if ii==0 or jj==0 or ii==M-1 or jj==N-1:return step+1#走道出口
                    visited.add( (ii, jj) )
                    queue.append( (ii, jj, step+1) )
        return -1



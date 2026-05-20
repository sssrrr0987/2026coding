# week12-1a.py 學習計畫 graph - DFS P1
# leetcode 841. Keys and Rooms
# 房間裡有鑰匙,可以再開新房間。最後能開全部房間嗎
# DFS Depth First Search 通常會用stack 或 function stack(函式呼叫)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]#存等等要去的房間,第一間去0號房
        visited = set()#用set存那些房間去過
        visited.add(0)#第一間去0號房
        while stack:#
            now = stack.pop()#去要去的房間
            for k in rooms[now]:#拿該房間中的鑰匙(代表之後能去那間房)
                if k in visited:continue#檢查這房間去過沒
                stack.append(k)#沒去過 加入等等去
                visited.add(k)#因為等等要去
        return len(rooms) == len(visited) #長度一樣代表都去過
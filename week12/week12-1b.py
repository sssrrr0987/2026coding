# week12-1b.py 學習計畫 graph - DFS P1
# leetcode 841. Keys and Rooms
# 房間裡有鑰匙,可以再開新房間。最後能開全部房間嗎
# DFS Depth First Search 通常會用stack 或 function stack(函式呼叫)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()#用set存那些房間去過
        def helper(now):#自訂義函式取代stack
            for k in rooms[now]:#拿該房間中的鑰匙(代表之後能去那間房)
                if k not in visited:#檢查這房間去過沒
                    visited.add(k)#因為等等要去
                    helper(k)
        visited.add(0)#第一間去0號房
        helper(0)#
        return len(rooms) == len(visited) #長度一樣代表都去過
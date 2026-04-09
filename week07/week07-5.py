# week07-5.py 學習計畫 Queue P1
# leetcode 933. Number of Recent Calls
# 
class RecentCounter:

    def __init__(self):#建構子
        #python 有 collections.deque
        #Double End Queue 簡稱deque()
        self.queue = deque()#宣告一個物件裡用self找到的queue變數
        
    def ping(self, t: int) -> int:
        self.queue.append(t)#右邊塞一個數
        while self.queue[0] < t-3000:#看是否最左邊的值有無超過時間範圍
            self.queue.popleft()#最左邊吐掉
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
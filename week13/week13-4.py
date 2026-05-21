# week13-4.py 學習計畫 Heap/Priority Queue P2
# leetcode 2336. Smallest Number in Infinite Set
# 找到最小的數
class SmallestInfiniteSet:

    def __init__(self):#建構子,準備資料結構
        self.now = 1#慢慢增加的數
        self.heap = []#資料結構,會吐出最小的數
        self.s = set()#避免heap中重複值

    def popSmallest(self) -> int:#會吐出最小的數
        if self.heap:#如果資料結構,已有一個較小值
            self.s.remove(self.heap[0])#將set中最小值也吐出
            return heappop(self.heap)#透過heap取最小值
        self.now += 1#不然 慢慢往上加
        return self.now - 1

    def addBack(self, num: int) -> None:
        if num < self.now and num not in self.s:#另外處理比較小的數
            self.s.add(num)
            heappush(self.heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
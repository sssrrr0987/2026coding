# week07-6.py 學習計畫 Queue P2
# leetcode 649. Dota2 Senate
# 由左到右,輪到的人能消滅一個敵人,直到剩一個陣營
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        print(senate, type(senate))
        print(list(senate), type(list(senate)))#觀察str變list

        queue = deque(list(senate))
        print(queue, type(queue))#觀察list變deque

        banR, banD = 0, 0#R跟D當前消滅次數
        R, D = senate.count('R'), senate.count('D')#各有幾人
        while queue:#看還有沒有人排隊
            now = queue.popleft()#目前的人
            if now == 'R':
                if banR > 0:#看自己陣營有沒有被消滅
                    banR -= 1
                    R -= 1
                else:
                    banD += 1
                    queue.append(now)#沒死就繼續排隊
            else:
                if banD > 0:
                    banD -= 1
                    D -= 1
                else:
                    banR += 1
                    queue.append(now)
            if R==0: return 'Dire'
            if D==0: return 'Radiant' 



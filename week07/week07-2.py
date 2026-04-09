# week07-2.py 學習計畫 Stack P2
# leetcode 735. Asteroid Collision
# 正的向右撞,副的向左撞,大撞小小不見，一樣大都不見
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for i in asteroids:
            if i>0:#往右撞先存起來
                ans.append(i)
            else :
                while ans and ans[-1]>0:#往左撞時確認前一項是否往右撞,撞到結束為止
                    if ans[-1] == -i:#一樣大一起不見
                        ans.pop()
                        i = 0
                        break
                    elif ans[-1] > -i:#左邊大右邊不見
                        i = 0
                        break
                    else:#右邊大一直往左撞
                        ans.pop()
                if i!= 0: ans.append(i)#如果還沒不見就存下
        return ans 
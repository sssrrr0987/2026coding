# week13-5.py 學習計畫 Heap/Priority Queue P3
# leetcode 2542. Maximum Subsequence Score
# 挑k個index,讓nums1對應的k個數相加,再乘min(nums2對應k個數)希望最大
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        N = len(nums1)
        a = [ (nums2[i], nums1[i]) for i in range(N)] #左右合併成(i,j)

        a.sort(reverse=True)#大到小排好
        #print(a)
        heap = [a[i][1] for i in range(k)]
        heapify(heap)#之後將小到大依序退掉 nums1的這k個數,換加入新的n1,n2組
        total = sum(heap)
        ans = total * a[k-1][0]#前k項的nums1及對應最小的nums2相乘

        for i in range(k, len(nums2)):#後面將加入的數
            n2, n1 = a[i]#將加入的對應的數
            heappush(heap, n1)#加1
            total += n1 - heappop(heap)#加1、吐1
            ans = max(ans, total*n2)#更新答案
        return ans
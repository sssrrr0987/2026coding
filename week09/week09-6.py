# week09-6.py 學習計畫 Linked List P2
# 328. Odd Even Linked List
# 先奇數index值在前 後偶數index值
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []#偷用陣列的index來判斷奇偶，再塞入新Linked List
        while head:
            a.append(head.val)
            head = head.next
        N = len(a)
        now = ans = ListNode()
        for i in range(0, N, 2):
            now.next = ListNode(a[i])
            now = now.next
        for i in range(1, N, 2):
            now.next = ListNode(a[i])
            now = now.next
        return ans.next
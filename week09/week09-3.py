# week09-3.py 學習計畫 Linked List P3 用函式呼叫函式Recursion
# week09-2.py 學習計畫 Linked List P3
# 206. Reverse Linked List
# 反轉Linked list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:return head #終止條件
        head2 = head.next
        ans = self.reverseList(head.next)
        head2.next, head.next = head, None
        return ans

        # a = []#轉陣列
        # while head:
        #     a.append( head.val )
        #     head = head.next
        # print(a)
        # now = ans = ListNode()#建Linked List
        # N = len(a)
        # for i in range(N-1, -1, -1):
        #     now.next = ListNode(a[i])
        #     now = now.next
        # return ans.next
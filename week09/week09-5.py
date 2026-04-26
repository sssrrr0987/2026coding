# week09-5.py 學習計畫 Linked List P1
# 2095. Delete the Middle Node of a Linked List
# 刪除中間的node
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:return None#特例如果只有1值
        prev = fast = slow = head #
        while fast != None and fast.next != None: #兔子還沒到終點
            fast = fast.next.next
            prev = slow #烏龜走之前的位置
            slow = slow.next
        #print(slow.val)#兔子到終點時,烏龜在中間
        prev.next = slow.next
        return head
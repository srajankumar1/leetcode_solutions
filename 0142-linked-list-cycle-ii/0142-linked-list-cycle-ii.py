# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if head==None:
            return None
        
        slow,fast,ptr=head,head,head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                while ptr!=slow:
                    ptr=ptr.next
                    slow=slow.next
                return ptr

        return None
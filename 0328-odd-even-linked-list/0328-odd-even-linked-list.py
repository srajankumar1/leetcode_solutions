# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        oddh=head
        evenh=head.next
        evenstart=evenh

        while evenh and evenh.next:
            oddh.next=oddh.next.next
            evenh.next=evenh.next.next
            oddh=oddh.next
            evenh=evenh.next

        oddh.next=evenstart

        return head
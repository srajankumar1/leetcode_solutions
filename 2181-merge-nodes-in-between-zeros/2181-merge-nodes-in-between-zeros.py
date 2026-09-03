# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        dummy=ListNode(-1)
        ans=dummy
        curr=head.next
        sum=0
        while curr:
            if curr.val==0:
                temp=ListNode(sum)
                dummy.next=temp
                dummy=dummy.next
                sum=0
            else:
                sum+=curr.val
            curr=curr.next
        return ans.next
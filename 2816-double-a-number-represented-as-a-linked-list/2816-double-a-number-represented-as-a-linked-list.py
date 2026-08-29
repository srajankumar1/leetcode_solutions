# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        def dfs(node):
            if not node:
                return 0
            carry=dfs(node.next)
            val=node.val*2+carry
            node.val=val%10
            return val//10

        carry=dfs(head)
        if carry:
            new=ListNode(carry)
            new.next=head
            head=new
        return head
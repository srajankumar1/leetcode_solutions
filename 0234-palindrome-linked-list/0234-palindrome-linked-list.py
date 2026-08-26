# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        stack=[]
        ptr=head
        while ptr:
            stack.append(ptr.val)
            ptr=ptr.next
        
        ptr2=head
        while ptr2:
            val1=ptr2.val
            val2=stack.pop()
            if val1!=val2:
                return False
            ptr2=ptr2.next

        return True
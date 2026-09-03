# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sizeLL(self,head):
        curr=head
        count=0
        while curr:
            count+=1
            curr=curr.next
        return count

    def reverseLL(self,head):
        curr=head
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev

    def nextLargerNodes(self, head):
        size=self.sizeLL(head)
        arr=[0]*size
        nhead=self.reverseLL(head)
        
        st=[]
        st.append(nhead.val)
        curr=nhead.next
        ptr=size-2
        
        while ptr>=0:
            ele=curr.val
            curr=curr.next
            while len(st)>0 and st[-1]<=ele:
                st.pop()
            if len(st)==0:
                arr[ptr]=0
            else:
                arr[ptr]=st[-1]
            
            st.append(ele)
            ptr-=1
        
        return arr
class Solution(object):
    def rob(self, nums):
        prev=0
        curr=0
        for n in nums:
            temp=max(curr,prev+n)
            prev=curr
            curr=temp
        return curr
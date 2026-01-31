class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        count=0
        while left<right:
            left>>=1
            right>>=1
            count+=1
        return left<<count
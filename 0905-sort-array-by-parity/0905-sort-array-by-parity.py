class Solution:
    def sortArrayByParity(self, nums):
        res=[]
        for x in nums:
            if x%2==0:
                res.append(x)
        for x in nums:
            if x%2==1:
                res.append(x)
        return res
class Solution(object):
    def singleNonDuplicate(self, nums):
        d={}
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        for key in d:
            if d[key]==1:
                return key
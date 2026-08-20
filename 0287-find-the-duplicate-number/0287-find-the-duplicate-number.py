class Solution(object):
    def findDuplicate(self, nums):
        d={}
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        for key in d:
            if d[key]>=2:
                return key
        return -1
class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        l=[]
        count=0
        for i in nums:
            if i==target:
                l.append(count)
            count+=1
        return l
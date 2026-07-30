class Solution(object):
    def findPeakElement(self, nums):
        max=nums[0]
        index=0
        for i in range(1,len(nums)):
            if nums[i]>max:
                max=nums[i]
                index=i
        return index
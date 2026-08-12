class Solution(object):
    def maxAscendingSum(self, nums):
        total=nums[0]
        curr=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                curr+=nums[i]
            else:
                curr=nums[i]
            if curr>total:
                total=curr
        return total
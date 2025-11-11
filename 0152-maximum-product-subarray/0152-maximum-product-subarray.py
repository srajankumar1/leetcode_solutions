class Solution:
    def maxProduct(self, nums):
        curr_max=nums[0]
        curr_min=nums[0]
        result=nums[0]
        
        for i in range(1,len(nums)):
            n=nums[i]
            temp_max=max(n,n*curr_max,n*curr_min)
            temp_min=min(n,n*curr_max,n*curr_min)
            curr_max,curr_min=temp_max,temp_min
            result=max(result,curr_max)
        
        return result
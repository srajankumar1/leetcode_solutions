class Solution(object):
    def maxSubArray(self, nums):
        max_sum=nums[0]
        current_sum=0
        for n in nums:
            current_sum+=n
            max_sum=max(max_sum,current_sum)
            
            if current_sum<0:
                current_sum=0
        
        return max_sum
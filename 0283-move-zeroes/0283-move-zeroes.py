class Solution:
    def moveZeroes(self, nums):
        lastNonZero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[lastNonZero],nums[i]=nums[i],nums[lastNonZero]
                lastNonZero+=1
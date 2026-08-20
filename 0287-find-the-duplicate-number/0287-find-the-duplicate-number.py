class Solution(object):
    def findDuplicate(self, nums):
        for i in range(len(nums)):
            ele=nums[i]
            ele=abs(ele)
            if nums[ele]>0:
                nums[ele]=-nums[ele]
            else:
                return ele
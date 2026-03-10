class Solution(object):
    def search(self, nums, target):
        index=-1
        for i in range(len(nums)):
            if nums[i]==target:
                index=i
        return index
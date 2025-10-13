class Solution(object):
    def searchInsert(self, nums, target):
        idx=0
        i=0
        lgt=len(nums)
        if target not in nums:
            while i<lgt:
                if nums[i]<target:
                    i+=1
                    idx=i
                else:
                    idx=i
                    break

        else:
            idx=nums.index(target)
        return idx
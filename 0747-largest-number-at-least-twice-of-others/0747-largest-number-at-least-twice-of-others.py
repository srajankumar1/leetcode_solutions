class Solution(object):
    def dominantIndex(self, nums):
        max1=nums[0]
        max2=float('-inf')
        i=0
        maxi=0
        for i in range(1,len(nums)):
            if nums[i]>max1:
                max2=max1
                max1=nums[i]
                maxi=i
            elif nums[i]>max2:
                max2=nums[i]
            i+=1
        if max1 >= max2*2:
            return maxi
        else:
            return -1

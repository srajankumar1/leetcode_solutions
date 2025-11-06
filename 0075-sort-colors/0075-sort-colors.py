class Solution:
    def sortColors(self, nums):
        count0=count1=count2=0
        for n in nums:
            if n==0:
                count0+=1
            elif n == 1:
                count1+=1
            else:
                count2+=1
        for i in range(len(nums)):
            if i<count0:
                nums[i]=0
            elif i<count0+count1:
                nums[i]=1
            else:
                nums[i]=2

        return nums
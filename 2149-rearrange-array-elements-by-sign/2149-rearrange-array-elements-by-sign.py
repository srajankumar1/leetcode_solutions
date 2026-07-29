class Solution(object):
    def rearrangeArray(self, nums):
        pos=[]
        neg=[]
        for num in nums:
            if num>0:
                pos.append(num)
            else:
                neg.append(num)
        p=0
        n=0
        
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=pos[p]
                p+=1
            else:
                nums[i]=neg[n]
                n+=1
        
        return nums
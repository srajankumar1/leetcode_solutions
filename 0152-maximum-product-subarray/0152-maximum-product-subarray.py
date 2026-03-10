class Solution:
    def maxProduct(self, nums):
        '''        
        maxx=nums[0]
        for i in range(len(nums)):
            prod=1
            for j in range(i,len(nums)):
                prod*=nums[j]
                maxx=max(prod,maxx)
        return maxx
        '''
        min_prod=nums[0]
        max_prod=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            num=nums[i]
            temp=max(num,num*max_prod,num*min_prod)
            min_prod=min(num,num*max_prod,num*min_prod)
            max_prod=temp
            res=max(res,max_prod)
        return res


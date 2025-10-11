class Solution(object):
    def twoSum(self, nums, target):
        d={}
        i=0
        for num in nums:
            next=target-num
            if next in d:
                return(d[next],i)
            d[num]=i
            i+=1
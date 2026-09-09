class Solution(object):
    def maxProduct(self, nums):
        fmax=-1
        smax=-1
        for num in nums:
            if num>fmax:
                smax=fmax
                fmax=num
            elif num>smax:
                smax=num
        return (fmax-1)*(smax-1)
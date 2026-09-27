class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d={}
        i=0
        for num in nums:
            if num in d:
                if abs(d[num]-i)<=k:
                    return True
            d[num]=i
            i+=1
        return False
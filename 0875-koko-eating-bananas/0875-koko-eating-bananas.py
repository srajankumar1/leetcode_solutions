class Solution:
    def minEatingSpeed(self, piles, h):
        l=1
        r=max(piles)
        while l<r:
            m=(l+r)//2
            hours=0
            for p in piles:
                hours+=(p+m-1)//m
            if hours>h:
                l=m+1
            else:
                r=m
        return l
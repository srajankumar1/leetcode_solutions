class Solution:
    def maximumUnits(self,boxTypes,truckSize):
        boxTypes.sort(key=lambda x:-x[1])
        ans=0
        for b,u in boxTypes:
            if truckSize==0:
                break
            take=min(b,truckSize)
            ans+=take*u
            truckSize-=take
        return ans
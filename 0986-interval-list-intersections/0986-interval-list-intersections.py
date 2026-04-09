class Solution:
    def intervalIntersection(self, firstList, secondList):
        i=0
        j=0
        res=[]
        while i<len(firstList) and j<len(secondList):
            a1,a2=firstList[i]
            b1,b2=secondList[j]
            start=max(a1,b1)
            end=min(a2,b2)
            if start<=end:
                res.append([start,end])
            if a2<b2:
                i+=1
            else:
                j+=1
        return res
class Solution(object):
    def findLucky(self, arr):
        d={}
        for num in arr:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        max=-1
        for key in d:
            if d[key]==key:
                if key>max:
                    max=key
        return max
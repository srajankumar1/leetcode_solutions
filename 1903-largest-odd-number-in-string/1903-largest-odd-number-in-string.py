class Solution(object):
    def largestOddNumber(self, num):
        end=-1
        i=0
        for i in range(len(num)-1,-1,-1):
            if (int(num[i])%2)==1:
                end=i
                break
        start=0
        while(start<=end and num[start]=='0'):
            start+=1
        return num[start:end+1]
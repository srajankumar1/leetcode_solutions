class Solution(object):
    def maxPower(self, s):
        maxi=1
        count=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
                maxi=max(maxi,count)
            else:
                count=1
        return maxi
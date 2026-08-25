class Solution(object):
    def isAnagram(self, s, t):
        l1={}
        l2={}
        for char in s:
            if char in l1:
                l1[char]+=1
            else:
                l1[char]=1
        for char in t:
            if char in l2:
                l2[char]+=1
            else:
                l2[char]=1
        return l1==l2
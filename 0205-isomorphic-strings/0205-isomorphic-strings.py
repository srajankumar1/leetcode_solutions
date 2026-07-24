class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        m1=[0]*256
        m2=[0]*256
        n=len(s)

        for i in range(n):
            if m1[ord(s[i])] != m2[ord(t[i])]:
                return False
            m1[ord(s[i])]=i+1
            m2[ord(t[i])]=i+1
        return True
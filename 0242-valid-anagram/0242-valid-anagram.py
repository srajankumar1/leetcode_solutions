class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        freq=[0]*26
        s=s.upper()
        t=t.upper()

        for char in s:
            freq[ord(char)-ord('A')]+=1
        for char in t:
            freq[ord(char)-ord('A')]-=1

        for ele in freq:
            if ele!=0:
                return False
        return True
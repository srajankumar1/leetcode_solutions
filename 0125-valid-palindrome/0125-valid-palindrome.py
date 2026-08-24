class Solution(object):
    def isPalindrome(self, s):
        if len(s)==1:
            return True
        s1=""
        for i in range(len(s)):
            ch=s[i]
            if ch>='a' and ch<='z':
                s1+=ch
            elif ch>='A' and ch<='Z':
                s1+=ch.lower()
            elif ch>='0' and ch<='9':
                s1+=ch
            
        if s1==s1[::-1]:
            return True
        else:
            return False
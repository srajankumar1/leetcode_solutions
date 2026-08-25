class Solution(object):
    def minAddToMakeValid(self, s):
        o=0
        c=0
        for char in s:
            if char=='(':
                o+=1
            else:
                if o>0:
                    o-=1
                else:
                    c+=1
        return o+c
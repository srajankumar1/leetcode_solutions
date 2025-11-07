class Solution(object):
    def findAnagrams(self, s, p):
        res=[]
        ls,lp=len(s),len(p)
        if lp>ls:
            return res
        
        target=[0]*26
        window=[0]*26

        for ch in p:
            target[ord(ch)-97]+=1
        for i in range(lp):
            window[ord(s[i])-97]+=1

        if window==target:
            res.append(0)

        for i in range(lp, ls):
            window[ord(s[i]) - 97]+=1
            window[ord(s[i-lp])-97]-=1
            if window==target:
                res.append(i-lp+1)
        return res
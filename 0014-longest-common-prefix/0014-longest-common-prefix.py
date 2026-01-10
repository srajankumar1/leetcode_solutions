class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        pref=strs[0]
        for s in strs[1:]:
            i=0
            while i<len(pref) and i<len(s) and pref[i]==s[i]:
                i+=1
            pref=pref[:i]
            if not pref:
                break
        return pref
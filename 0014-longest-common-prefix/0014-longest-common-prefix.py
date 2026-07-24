class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        strs.sort()
        start=strs[0]
        end=strs[-1]
        ans=[]

        for i in range(min(len(start),len(end))):
            if start[i]!=end[i]:
                return "".join(ans)
            ans.append(start[i])
        return "".join(ans)
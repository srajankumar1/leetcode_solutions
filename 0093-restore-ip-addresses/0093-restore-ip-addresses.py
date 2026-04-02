class Solution:
    def restoreIpAddresses(self, s):
        res=[]
        def dfs(start,parts,path):
            if parts==4 and start==len(s):
                res.append(".".join(path))
                return
            if parts==4 or start==len(s):
                return
            for i in range(1,4):
                if start+i>len(s):
                    break
                seg=s[start:start+i]
                if (seg[0]=="0" and len(seg)>1) or int(seg)>255:
                    continue
                dfs(start+i,parts+1,path+[seg])
        dfs(0,0,[])
        return res
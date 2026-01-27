class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        mp={
            "2":"abc","3":"def","4":"ghi","5":"jkl",
            "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }
        res=[""]
        for d in digits:
            tmp=[]
            for p in res:
                for c in mp[d]:
                    tmp.append(p+c)
            res=tmp
        return res
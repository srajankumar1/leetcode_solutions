class Solution:
    def wordBreak(self, s, wordDict):
        memo={}
        
        def dfs(start):
            if start==len(s):
                return True
            if start in memo:
                return memo[start]
            
            for w in wordDict:
                if s.startswith(w,start):
                    if dfs(start+len(w)):
                        memo[start]=True
                        return True
            
            memo[start]=False
            return False
        
        return dfs(0)
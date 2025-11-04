class Solution(object):
    def minSwaps(self, grid):
        n=len(grid)
        right=[]
        for row in grid:
            r=-1
            for j in range(n-1, -1, -1):
                if row[j]==1:
                    r=j
                    break
            right.append(r)
        ans=0
        for i in range(n):
            k=i
            while k<n and right[k]>i:
                k+=1
            if k==n:
                return -1
            ans+=(k-i)
            val=right.pop(k)
            right.insert(i, val)
        return ans
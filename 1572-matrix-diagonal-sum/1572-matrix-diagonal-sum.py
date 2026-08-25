class Solution(object):
    def diagonalSum(self, mat):
        n=len(mat)
        psum=0
        ssum=0
        for i in range(n):
            psum+=mat[i][i]
            ssum+=mat[i][n-1-i]
        if n%2==1:
            ssum-=mat[n//2][n//2]
        return psum+ssum
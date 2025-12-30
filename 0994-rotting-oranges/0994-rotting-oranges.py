class Solution:
    def orangesRotting(self,grid):
        rows=len(grid)
        cols=len(grid[0])
        q=[]
        fresh=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        minutes=0
        while q and fresh>0:
            newq=[]
            for x,y in q:
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx,ny=x+dx,y+dy
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        fresh-=1
                        newq.append((nx,ny))
            q=newq
            minutes+=1
        return minutes if fresh==0 else -1
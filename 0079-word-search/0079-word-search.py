from collections import Counter

class Solution:
    def exist(self, board, word):
        if not board or not board[0]:
            return False
        m = len(board)
        n = len(board[0])
        L = len(word)
        if m * n < L:
            return False
        cb = Counter(ch for row in board for ch in row)
        cw = Counter(word)
        for k,v in cw.items():
            if cb[k] < v:
                return False
        rows, cols = m, n

        def dfs(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == L - 1:
                return True
            tmp = board[i][j]
            board[i][j] = None
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and board[ni][nj] is not None:
                    if dfs(ni, nj, k + 1):
                        board[i][j] = tmp
                        return True
            board[i][j] = tmp
            return False

        start = word[0]
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == start:
                    if dfs(i, j, 0):
                        return True
        return False
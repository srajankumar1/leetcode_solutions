class Solution:
    def solveSudoku(self, board):
        rows = [0]*9
        cols = [0]*9
        boxes = [0]*9
        empties = []
        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == ".":
                    empties.append((r,c))
                else:
                    d = ord(ch)-ord("0")
                    bit = 1<<d
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[(r//3)*3+(c//3)] |= bit

        def avail_bits(r,c):
            used = rows[r] | cols[c] | boxes[(r//3)*3+(c//3)]
            return (~used) & 0x3FE

        def select_next():
            best_i = -1
            best_bits = 0
            best_cnt = 10
            for i,(r,c) in enumerate(empties):
                if board[r][c] != ".":
                    continue
                bits = avail_bits(r,c)
                if bits == 0:
                    return -1,0
                if hasattr(int,"bit_count"):
                    cnt = bits.bit_count()
                else:
                    cnt = bin(bits).count("1")
                if cnt < best_cnt:
                    best_cnt = cnt
                    best_i = i
                    best_bits = bits
                    if cnt == 1:
                        break
            return best_i,best_bits

        n = len(empties)
        def dfs(filled):
            if filled == n:
                return True
            idx,bits = select_next()
            if idx == -1:
                return False
            r,c = empties[idx]
            bidx = (r//3)*3+(c//3)
            while bits:
                bit = bits & -bits
                bits -= bit
                d = bit.bit_length()-1
                board[r][c] = chr(d+ord("0"))
                rows[r] |= bit
                cols[c] |= bit
                boxes[bidx] |= bit
                if dfs(filled+1):
                    return True
                board[r][c] = "."
                rows[r] &= ~bit
                cols[c] &= ~bit
                boxes[bidx] &= ~bit
            return False

        dfs(0)
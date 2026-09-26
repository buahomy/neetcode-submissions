class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
                
        rows, cols = len(board), len(board[0])      
        # Recursive calls to crowd out all invalid cases 
        # i -> valid character      
        def backtrack(r, c, i):
            if i == len(word):
                return True
            # go off top, left, right, bottom, char on board not matched with curr letter, the visited   
            if (r < 0 or c < 0 or r >= rows or c>= cols or 
            word[i] != board[r][c] or board[r][c] == '#'):
                return False

            #*start here
            board[r][c] = '#' # marked as visited 
            # blindly try 4 directions: under, above, right, left 
            output = (backtrack(r + 1, c, i + 1) or 
            backtrack(r - 1, c, i + 1) or
            backtrack(r, c + 1, i + 1) or
            backtrack(r, c - 1, i + 1))

            board[r][c] = word[i] # undo (backtrack)
            return output

        # 2D
        for r in range(rows): # recursively line by line 
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False            


             
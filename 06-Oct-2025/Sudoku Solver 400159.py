# Problem: Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        norm = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    cx = ceil((i) // 3)
                    cj = ceil((j) // 3)
                    nm = int(board[i][j])
                    norm[(i,10)].add(nm)
                    norm[(j,11)].add(nm)
                    norm[(cx,cj)].add(nm)

        def do(i = 0 , j = 0):
            if i == 8 and j == 9:
                return True

            nxti = nxtj = 0
            if j == 8 and i != 8:
                nxti = i + 1
                nxtj = 0
            else:
                nxti = i
                nxtj = j + 1

            if board[i][j] != ".":
                return do(nxti , nxtj)
            vl = False  
            cx = ceil((i) // 3)
            cj = ceil((j) // 3)
            for nm in range(1,10):
                if (nm not in norm[(cx,cj)] and nm not in norm[(i,10)] and nm not in norm[(j,11)]):
                    norm[(cx,cj)].add(nm)
                    norm[(i,10)].add(nm)
                    norm[(j,11)].add(nm)
                    board[i][j] = str(nm)
                    vl = do(nxti , nxtj)
                    if not vl:
                        board[i][j] = "."
                        norm[(cx,cj)].remove(nm)
                        norm[(i,10)].remove(nm)
                        norm[(j,11)].remove(nm)

                if vl:
                    return vl


        do()



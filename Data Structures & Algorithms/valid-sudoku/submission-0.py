class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=defaultdict(set)
        col=defaultdict(set)
        cube=defaultdict(set)

        for r in range(9):
            for c in range(9):
                val=board[r][c] # row-wise traversing

                if val=='.':
                    continue

                if (val in row[r] or val in col[c] or val in cube[(r//3,c//3)]):
                    return False

                row[r].add(val)
                col[c].add(val)
                cube[(r//3,c//3)].add(val)

        return True

board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

obj=Solution()
soln=obj.isValidSudoku(board)
print(soln)
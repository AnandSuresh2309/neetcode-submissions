class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        box_dict = defaultdict(set)
        for i in range(9):

            row_set = set()
            col_set = set()
            
            for j in range(9):

                if board[i][j] != ".":
                    if board[i][j] in row_set:
                        return False
                    else:
                        row_set.add(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in col_set:
                        return False
                    else:
                        col_set.add(board[j][i])

                if board[i][j] != ".":
                    if board[i][j] in box_dict[(i//3, j//3)]:
                        return False
                    else:
                        box_dict[(i//3, j//3)].add(board[i][j])

        return True

                
        
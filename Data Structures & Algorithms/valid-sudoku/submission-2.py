class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        count = defaultdict(set)

        for r in range(len(board)):
            count['row'] = set()
            for c in range(len(board[r])):
                if board[r][c]!=".":
                    if board[r][c] in count['row']:
                        return False
                    count['row'].add(board[r][c])
        
        for r in range(len(board)):
            count['col'] = set()
            for c in range(len(board[r])):
                if board[c][r]!=".":
                    if board[c][r] in count['col']:
                        return False
                    count['col'].add(board[c][r])

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c]!=".":
                    if board[r][c] in count[(r//3,c//3)]:
                        return False
                    count[(r//3,c//3)].add(board[r][c])
        
        return True
        
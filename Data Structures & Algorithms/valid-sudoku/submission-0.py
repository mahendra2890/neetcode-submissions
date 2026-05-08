class Solution:
    def isRowValid(self, board: List[List[str]], index: int) -> bool:
        # index'th row: board[index][0:9]
        rowFreq = [0]*9
        for i in range(0,9,1):
            if (board[index][i]) != ".":
                rowFreq[int(board[index][i])-1]+=1
        for item in rowFreq:
            if item > 1:
                return False
        return True
        
    def isColumnValid(self, board: List[List[str]], index: int) -> bool:
        # index'th column: board[0:9][index]
        colFreq = [0]*9
        for i in range(0,9,1):
            if (board[i][index]) != ".":
                colFreq[int(board[i][index])-1]+=1
        for item in colFreq:
            if item > 1:
                return False
        return True

    def isBlockValid(self, board: List[List[str]], index: int) -> bool:
        # index'th block: 3X3 block starting from [(index//3)*3][(index*3)%9]
        blockFreq = [0]*9
        row=(index//3)*3
        col=(index*3)%9
        for i in range(0,3,1):
            for j in range(0,3,1):
                if (board[row+i][col+j]) != ".":
                    blockFreq[int(board[row+i][col+j])-1]+=1
        for item in blockFreq:
            if item > 1:
                return False
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9,1):
            if not self.isRowValid(board, i):
                return False
            if not self.isColumnValid(board, i):
                return False
            if not self.isBlockValid(board, i):
                return False
        return True
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0 

        board = [["."]*n for _ in range(n)]
        leftR = [0]*n
        lowerD = [0]*(2*n - 1)
        upperD = [0]*(2*n-1)

        self.solve(0, board, leftR, lowerD, upperD,n)
        return self.count

    def solve(self, col, board, leftR, lowerD, upperD, n):
        if col == n:
            self.count +=1

        for row in range(n):
            if(leftR[row] == 0 and upperD[n-1 + col - row] == 0 and lowerD[row + col] == 0):
                board[row][col] = "Q"
                leftR[row] = 1
                lowerD[row+col] = 1
                upperD[n-1 + col - row ] = 1

                self.solve(col+1, board, leftR, lowerD, upperD, n )

                board[row][col] = "."
                leftR[row] = 0
                lowerD[row+col] = 0
                upperD[n-1 + col - row ] = 0

                



        
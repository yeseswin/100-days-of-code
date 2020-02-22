n = 8

def isValidPosition(x,y,board):
    if x>=0 and y>=0 and x<n and y < n and board[x][y]==-1:
        return True

    return False

def printMatrix(matrix):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=' ')
        
        print()

    print()

def solve(currX,currY,moveX,moveY,matrix,pos):

    if pos == n**2:
        return True

    for i in range(n):
        newX=currX+moveX[i]
        newY=currY+moveY[i]
        if isValidPosition(newX,newY,matrix):
            matrix[newX][newY]=pos
            if(solve(newX,newY,moveX,moveY,matrix,pos+1)):
                return True
            
            matrix[newX][newY]=-1

    return False

if __name__ == "__main__":
    
    chessBoard=[[-1 for i in range(n)]for i in range(n)]
    # print(chessBoard)

    printMatrix(chessBoard)
    currX=0
    currY=0
    moveX=[1,2,2,1,-1,-2,-2,-1]
    moveY=[2,1,-1,-2,-2,-1,1,2]
    chessBoard[0][0] =0
    if(solve(0,0,moveX,moveY,chessBoard,1)):
        printMatrix(chessBoard)
    else:
        print("No solution !");



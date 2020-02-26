n = 4

def printMatrix(matrix):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=' ')
        
        print()

    print()

def isValidPosition(x,y,matrix):

    for i in range(n):

        if matrix[x][i]==1:
            return False
    
    for i,j in zip(range(x,-1,-1),range(y,-1,-1)):
        if matrix[i][j] ==1:
            return False


    for i,j in zip(range(x,n,1),range(y,-1,-1)):
        if matrix[i][j] ==1:
            return False

    return True

def solve(matrix,y):

    if y>=n:
        return True

    for i in range(n):

        if isValidPosition(i,y,matrix) :
            
            matrix[i][y]=1

            if(solve(matrix,y+1)):
                return True
    
            matrix[i][y]=0

    return False

if __name__ == "__main__":
    
    chessBoard=[[0 for i in range(n)]for i in range(n)]

    if(solve(chessBoard,0)):
        printMatrix(chessBoard)

    else:
        print("No solution found")

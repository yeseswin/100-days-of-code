n=4

def isValidPosition(x,y,matrix):
    if x>=0 and y>=0 and x<n and y<n and matrix[x][y]!=0:
        return True
    
    return False

def printMatrix(matrix):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=' ')
        
        print()

    print()

def solve(matrix,x,y,solution):

    if x==n-1 and y==n-1:
        return True

    if isValidPosition(x,y,matrix):
        solution[x][y]=1

        if solve(matrix,x+1,y,solution):
            return True

        if solve(matrix,x,y+1,solution):
            return True

    
        solution[x][y]=0

    return False

if __name__ == "__main__":
    
    maze = [ [1, 0, 0, 0], 
             [1, 1, 0, 1], 
             [0, 1, 0, 0], 
             [1, 1, 1, 1] ]

    solution=[[0 for i in range(n)]for i in range(n)]
    
    if solve(maze,2,1,solution):
        printMatrix(solution)
        print("Ate my cheese !")
    else:
        print("I am Stuck . There is no cheese master! XD ")



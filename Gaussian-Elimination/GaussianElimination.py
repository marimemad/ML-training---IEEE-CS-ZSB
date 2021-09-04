def get_zero(matrix,val,row_index):
    row1=matrix[row_index]
    row2=matrix[row_index-1]
    for i in range(len(row1)):
        row1[i]=round(val*row2[i]+row1[i],1)

    matrix[row_index]=row1
    return (matrix)

def substitute(matrix,n):
    result={}
    result[n-1]=round(matrix[n-1][n]/matrix[n-1][n-1])

    for row in range(n-2,-1,-1):
        sum=0
        for col in range(n-1,row,-1):
            sum+=(matrix[row][col]*result[col])

        result[row]=round((matrix[row][n]- sum)/matrix[row][row])
    return(result)

def gaussian_elimination(matrix,n):
    for row in range(1,n):
        for col in range(row):
            if matrix[row][col]==0:
                continue
            val=matrix[row][col]/matrix[row-1][col]
            matrix=get_zero(matrix, -val, row)

    result=substitute(matrix,n)

    for i in range(0,n):
        print('X',i+1,'=',result[i])


if __name__ == '__main__':
    n=int(input('Number of variables: '))
    matrix=[]
    for i in range(n):
        row=list(map(int,input().split()))
        matrix.append(row)

    gaussian_elimination(matrix,n)

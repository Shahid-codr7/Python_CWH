# Multiplication of two 2-D Matrices same as Q6
def main():
    rows,cols=3,3
    print('Enter elements in matrix A')
    matrix_A=[[int(input(f'Enter element at ({rows},{cols})')) for j in range(cols)]for i in range(rows)]
    print(matrix_A)
    print('Enter elements in matrix B')
    matrix_B=[[int(input(f'Enter element at ({rows},{cols})')) for j in range(cols)]for i in range(rows)]
    print(matrix_B)
    Add(matrix_A,matrix_B)
def Add(matrix1,matrix2):
    rows=len(matrix1)
    cols=len(matrix1[0])
    print(rows," ||| ",cols)
    A=[[0 for j in range(cols)]for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            m = matrix1[i][j]*matrix2[j][i]
            
    print(A)
if __name__ == "__main__":
    main()
    
            
            

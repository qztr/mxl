# mxl - matrix library

# константы размерности
COLS,ROWS = 5,5

def set_consts(rows,cols):
    global C,R
    C,R = cols, rows

# функция создания нулевой матрицы размерности rows,cols
def define_Zmatrix(rows,cols):
    my_matrix = [([0]*cols) for i in range(rows)]
    return my_matrix
    
# функция создания единичной матрицы размерности rows,cols
def define_1matrix(rows,cols):
    my_matrix = [([1]*cols) for i in range(rows)]
    return my_matrix

# константы нулевой и единичной матриц
mZ = define_Zmatrix(COLS,ROWS)
m1 = define_Zmatrix(COLS,ROWS)

# внутрнее перемножение матриц
def mydot(v1, v2):
     return sum([x*y for x,y in zip(v1, v2)])

# перемножение матрицы [M] на скаляр [v]
def matmulvec(M, v):
    return [mydot(r,v) for r in M]

# сложение матриц
def matrix_addition(A, B):
    try:    
        """
        Adds two matrices and returns the sum
            :param A: The first matrix
            :param B: The second matrix
     
            :return: Matrix sum
        """
        # Section 1: Ensure dimensions are valid for matrix addition
        rowsA = len(A)
        colsA = len(A[0])
        rowsB = len(B)
        colsB = len(B[0])
        if rowsA != rowsB or colsA != colsB:
            raise ArithmeticError('Matrices are NOT the same size.')
     
        # Section 2: Create a new matrix for the matrix sum
        C = define_Zmatrix(rowsA, colsB)
     
        # Section 3: Perform element by element sum
        for i in range(rowsA):
            for j in range(colsB):
                C[i][j] = A[i][j] + B[i][j]
     
        return C
    except:
        print('Matrices are NOT the same size.')
        
# умножение матриц
def matrix_mul(A, B):
    try:    
        """
        Returns the product of the matrix A * B
            :param A: The first matrix - ORDER MATTERS!
            :param B: The second matrix
     
            :return: The product of the two matrices
        """
        # Section 1: Ensure A & B dimensions are correct for multiplication
        rowsA = len(A)
        colsA = len(A[0])
        rowsB = len(B)
        colsB = len(B[0])
        if colsA != rowsB:
            raise ArithmeticError(
                'Number of A columns must equal number of B rows.')
     
        # Section 2: Store matrix multiplication in a new matrix
        C = define_Zmatrix(rowsA, colsB)
        for i in range(rowsA):
            for j in range(colsB):
                total = 0
                for ii in range(colsA):
                    total += A[i][ii] * B[ii][j]
                C[i][j] = total
     
        return C
    except:
        print('Matrices are NOT the same size.')


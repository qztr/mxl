# mxl - matrix library

# константы размерности
COLS,ROWS = 5,5

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
m1 = define_1matrix(COLS,ROWS)

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
        
# проверка двух матриц на равенство
def check_matrix_equality(A, B):
    """
    Checks the equality of two matrices.
        :param A: The first matrix
        :param B: The second matrix
        :return: The boolean result of the equality check
    """
    # Section 1: First ensure matrices have same dimensions
    try:
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            return False
     
        # Section 2: Check element by element equality
        #            use tolerance if given
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != B[i][j]:
                    return False
        return True
    except:
        print("Something wrong with Matrices... enter enother ones")
        

# ========================================================

def determinant(matrix, mul = 1):
        """
        Определитель матрицы
        """
    
        
        width = len(matrix)
        
        if width == 1:
            return mul * matrix[0][0]
        else:
            sign = -1
            sum = 0
            
            for i in range(width):
                m = []
                for j in range(1, width):
                    buff = []
                    for k in range(width):
                        if k != i:
                            buff.append(matrix[j][k])
                    m.append(buff)
                sign *= -1
                sum += mul * determinant(m, sign * matrix[0][i])
            
            return sum
            

def minor(i, j, matrix):
        """
        Возвращает минор матрицы
        """

            
        matrix_minor = []
        for row in (matrix[:i]+matrix[i+1:]):
            matrix_minor.append(row[:j] + row[j+1:]) 
        
        return matrix_minor

def transposition(matrix):
        """
        Транспонирование матрицы
        """
        try:
        
            transpos_matrix = []
            I = len(matrix)
            J = len(matrix[0])
            
            for j in range(J):
                temp = []
                for i in range(I):
                    temp.append(matrix[i][j])
                transpos_matrix.append(temp)
            
            return transpos_matrix
        except:
            print("Something wrong with Matrix... enter enother one")

def union_matrix(matrix):
        """
        Союзная матрица
        """
        
        determ = determinant(matrix = matrix)
        
        transp_matrix = transposition(matrix)
        
        union = []
        
        for i in range(len(transp_matrix)):
            temp = []
            for j in range(len(transp_matrix[0])):
                minor_determ = (-1)**(i+1 + j+1) * determinant(matrix=minor(matrix = transp_matrix, i=i, j=j))
                temp.append(minor_determ)
            union.append(temp)
        
        return union

def dotAn(matrix, n):
        """
        Произведение матрицы на число
        """
        
        if type(n) == int or type(n) == float:
            mult = []
            for i in matrix:
                temp = []
                for j in i:
                    temp.append(round(j*n, 2))
                mult.append(temp)
            return mult

def inverse(matrix):
        """
        Обратная матрица
        """
        try:
            determ = determinant(matrix = matrix)
            
            if (determ != 0):
                inverse_matrix = dotAn(matrix = union_matrix(matrix), n = (1/determ))
                return inverse_matrix
            else:
                print("Матрица вырожденная\nОбратная для неё не существует")
                return 0
        except:
            print("Something wrong with Matrix... enter enother one")
            
# ==============================================================================        



















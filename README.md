<<<<<<< HEAD
 Matrix calculations
================

Installing:

    pip install -i https://test.pypi.org/simple/ qztr-mxl

----------
**В библиотеке реализованы следующие операции:**

1) Объявить константы 0 и единичной матриц
2) Умножение матрицы на скаляр
3) Сложение матриц одинакового размера
4) умножение матриц одинакового размера
5) вычисление определителя
6) сравнение на равенство
7) обратная матрица
----------
1. **Объявить константы 0 и единичной матриц**

Для начала имопртируем класс solver:

    from mxl import solver
	
Метод создания статической нулевой матрицы раземерности 5х5:

    matrixZ = solver.mZ # нулевая матрица
    matrix1 = solver.m1 # единичная матрица
    
    >>> matrixZ
    [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
	

Метод создания нулевой матрицы размерности C,R:

    matrix1 = solver.define_1matrix(C,R)
    matrixZ = solver.define_Zmatrix(C,R)
    
    >>> matrix1
    [[1, 1], [1, 1]]
    
Умножение матрицы на скаляр:

    s_mul = solver.matmulvec(M, v)
    
    >>> v = [1,2,3]
    >>> s_mul = solver.matmulvec(matrix1, v)
    >>> s_mul
    [3, 3]
    
Сложение матриц одинакового размера:
    
    add = solver.matrix_addition(A, B)
    
    >>> add = solver.matrix_addition(matrix1, matrix1)
    >>> add
    [[2, 2], [2, 2]]
    
Умножение матриц одинакового размера:

    m_mul = solver.matrix_mul(A, B)
    
    >>> y = [[3,3],[0,0]]
    >>> m_mul = solver.matrix_mul(matrix1, y)
    >>> m_mul
    [[3, 3], [3, 3]]
    
Вычисление определителя

    det = solver.determinant(matrix)
    
    >>> det = solver.determinant(matrix1)
    >>> det
    0

Сравнение на равенство

    check = solver.check_matrix_equality(A, B)
    
    >>> check = solver.check_matrix_equality(y, y)
    >>> check
    True
	
Обратная матрица

    inv = inverse(matrix)
    
    >>> inv = solver.inverse(matrix1)
    Матрица вырожденная
    Обратная для неё не существует
=======
 Matrix calculations
================

Installing:

    pip install -i https://test.pypi.org/simple/ qztr-mxl

----------
**В библиотеке реализованы следующие операции:**

1) Объявить константы 0 и единичной матриц
2) Умножение матрицы на скаляр
3) Сложение матриц одинакового размера
4) умножение матриц одинакового размера
5) вычисление определителя
6) сравнение на равенство
7) обратная матрица
----------
1. **Объявить константы 0 и единичной матриц**

Для начала имопртируем класс solver:

    from mxl import solver
	
Метод создания статической нулевой матрицы раземерности 5х5:

    matrixZ = solver.mZ # нулевая матрица
    matrix1 = solver.m1 # единичная матрица
    
    >>> matrixZ
    [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
	

Метод создания нулевой матрицы размерности C,R:

    matrix1 = solver.define_1matrix(C,R)
    matrixZ = solver.define_Zmatrix(C,R)
    
    >>> matrix1
    [[1, 1], [1, 1]]
    
Умножение матрицы на скаляр:

    s_mul = solver.matmulvec(M, v)
    
    >>> v = [1,2,3]
    >>> s_mul = solver.matmulvec(matrix1, v)
    >>> s_mul
    [3, 3]
    
Сложение матриц одинакового размера:
    
    add = solver.matrix_addition(A, B)
    
    >>> add = solver.matrix_addition(matrix1, matrix1)
    >>> add
    [[2, 2], [2, 2]]
    
Умножение матриц одинакового размера:

    m_mul = solver.matrix_mul(A, B)
    
    >>> y = [[3,3],[0,0]]
    >>> m_mul = solver.matrix_mul(matrix1, y)
    >>> m_mul
    [[3, 3], [3, 3]]
    
Вычисление определителя

    det = solver.determinant(matrix)
    
    >>> det = solver.determinant(matrix1)
    >>> det
    0

Сравнение на равенство

    check = solver.check_matrix_equality(A, B)
    
    >>> check = solver.check_matrix_equality(y, y)
    >>> check
    True
	
Обратная матрица

    inv = inverse(matrix)
    
    >>> inv = solver.inverse(matrix1)
	>>> inv
    Матрица вырожденная
    Обратная для неё не существует>>>>>>> readme

from envtest import my_mat_solve

from sympy.matrices import Matrix, MatrixSymbol

# Call function to solve the linear equation A*x=b symbolically

A = Matrix([[2, 1, 3], [4, 7, 1], [2, 6, 8]])
b = Matrix(MatrixSymbol('b', 3, 1))
x = my_mat_solve(A, b)

print(x)
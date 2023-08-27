import numpy as np
def sum_vector_complex(vector_a, vector_b):
    c = []
    if len(vector_a) == len(vector_b):
        for i in range(len(vector_a)):
            c.append(vector_a[i] + vector_b[i])
        return c
    return "Error, los vectores son de diferente tamaño"

def inv_add_vector_complex(vector):
    c = []
    for i in range(len(vector)):
        c.append((-vector[i]))
    return c

def mult_scalar_vector_complex(scalar, vector):
    c = []
    for i in range(len(vector)):
        c.append(scalar * vector[i])
    return c

def print_data(data):
    if isinstance(data[0], complex):  # Si es un vector
        print("[" + ", ".join(str(x) for x in data) + "]")
    else:  # Si es una matriz
        for fila in data:
            print(fila)


def sum_matrix_complex(matrix_a, matrix_b):
    filas = len(matrix_a)
    columnas = len(matrix_a[0])
    result_matrix = [[0j] * columnas for k in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            result_matrix[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result_matrix

def inv_add_matrix_complex(matrix):
    filas = len(matrix)
    columnas = len(matrix[0])
    for i in range(filas):
        for j in range(columnas):
            matrix[i][j] = -matrix[i][j]
    return matrix

def mult_scalar_matrix_complex(scalar,matrix):
    filas = len(matrix)
    columnas = len(matrix[0])
    for i in range(filas):
        for j in range(columnas):
            matrix[i][j] = scalar*matrix[i][j]
    return matrix

def transpose_matrix_complex(matrix):
    if isinstance(matrix[0], complex):
        return [[x] for x in matrix]
    filas = len(matrix)
    columnas = len(matrix[0])
    traspuesta = [[0j] * filas for k in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            traspuesta[j][i] = matrix[i][j]
    return traspuesta

def conjugate_matrix(matrix):
    if isinstance(matrix[0], complex):
        return [x.conjugate() for x in matrix]
    filas = len(matrix)
    columnas = len(matrix[0])
    conjugada = [[0j] * filas for k in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            conjugada[i][j] = matrix[i][j].conjugate()
    return conjugada
def adjoint_matrix(matrix):
    conjugada = conjugate_matrix(matrix)
    return transpose_matrix_complex(conjugada)


def mult_matrix(matrix_a, matrix_b):
    filas_a = len(matrix_a)
    columnas_a = len(matrix_a[0])
    filas_b = len(matrix_b)
    columnas_b = len(matrix_b[0])

    if columnas_a != filas_b:
        raise ValueError("Las matrices no son de tamaños compatibles para multiplicación")
    result_matrix = [[0j] * columnas_b for m in range(filas_a)]
    for i in range(filas_a):
        for j in range(columnas_b):
            sum_product = 0j
            for k in range(columnas_a):
                sum_product += matrix_a[i][k] * matrix_b[k][j]
            result_matrix[i][j] = sum_product
    return result_matrix

def matrix_action_vector(matrix, vector):
    result = mult_matrix(matrix, [[x] for x in vector])
    return [x[0] for x in result]

if __name__ == '__main__':
    print('Ejemplo suma de vectores complejos: ', sum_vector_complex([complex(-5,-5),complex(-4,4)],[complex(3,2),complex(5,1)]))
    print('Ejemplo inverso aditivo de un vector complejo: ', inv_add_vector_complex([complex(5,4),complex(2,4)]))
    print('Ejemplo multiplicación escalar con vector complejo: ', mult_scalar_vector_complex(5,[complex(5,4),complex(2,4)]))
    print('Ejemplo suma de matrices complejas: ')
    print_data(sum_matrix_complex([[complex(1, 2), complex(3, -1)],
                                             [complex(8, 4), complex(-2, 5)]],
                                  [[complex(-1, 1), complex(2, 3)],
                                            [complex(8, 6), complex(4, -2)]]))
    print('Ejemplo inversa aditivo de una matriz compleja: ')
    print_data(inv_add_matrix_complex([[complex(1, 2), complex(3, -1)],
                                       [complex(0, 4), complex(-2, 5)]]))
    print('Ejemplo multiplicación escalar con matriz compleja: ')
    print_data(mult_scalar_matrix_complex(5, [[complex(1, 2), complex(3, -1)],
                                              [complex(0, 4), complex(-2, 5)]]))
    print('Ejemplo traspuesta de vector complejo: ')
    print_data(transpose_matrix_complex([complex(1, 2), complex(3, -5)]))

    print('Ejemplo traspuesta de matriz compleja: ')
    print_data(transpose_matrix_complex([[complex(1, 2), complex(3, -5)],
                                         [complex(5, 4), complex(-2, 5)]]))
    print('Ejemplo conjugado de vector complejo: ')
    print_data(conjugate_matrix([complex(1, 2), complex(3, -5)]))

    print('Ejemplo conjugada de matriz compleja: ')
    print_data(conjugate_matrix([[complex(1, 2), complex(3, -5)],
                                 [complex(5, 4), complex(-2, 5)]]))

    print('Ejemplo adjunto de vector complejo: ')
    print_data(adjoint_matrix([complex(1, 2), complex(3, -5)]))

    print('Ejemplo adjunta de matriz compleja: ')
    print_data(adjoint_matrix([[complex(1, 2), complex(3, -5)],
                                 [complex(5, 4), complex(-2, 5)]]))
    print('Ejemplo producto de matrices complejas: ')
    print_data(mult_matrix([[complex(1, 2), complex(3, -1)],
                                   [complex(8, 4), complex(-2, 5)]],
                            [[complex(-1, 1), complex(2, 3)],
                                   [complex(8, 6), complex(4, -2)]]))
    print('Ejemplo de "acción" de una matriz compleja sobre un vector complejo: ')
    print_data(matrix_action_vector([[complex(1, 2), complex(3, 4)],
                                     [complex(8, 4), complex(-2, 5)]],
                                    [complex(-1, 1), complex(2, 3)]))























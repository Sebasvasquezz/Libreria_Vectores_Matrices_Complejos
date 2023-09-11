# Librería de Operaciones con Vectores y Matrices Complejos.

Esta librería de Python brinda funciones para llevar a cabo diferentes operaciones con vectores y matrices complejos. Esto abarca desde operaciones simples hasta transformaciones de sus representaciones y cálculos relacionados con sus características.

## Requisitos

- [PyCharm 3.11](https://www.jetbrains.com/pycharm/)

## Operaciones Incluidas

La librería consta de las siguientes operaciones para vectores y matrices complejos, los números complejos parte de cada vector o matriz se representan por medio del tipo "complex" de la librería numpy de python, donde la primera componente es la parte real y la segunda, la imaginaria:

1. **Adición de vectores complejos:** `sum_vector_complex(vector_a, vector_b)`
2. **Inverso (aditivo) de un vector complejo:** `inv_add_vector_complex(vector)`
3. **Multiplicación de un escalar por un vector complejo:** `(scalar, vector)`
4. **Adición de matrices complejas:** `sum_matrix_complex(matrix_a, matrix_b)`
5. **Inversa (aditiva) de una matriz compleja.:** `inv_add_matrix_complex(matrix)`
6. **Multiplicación de un escalar por una matriz compleja:** `mult_scalar_matrix_complex(scalar,matrix)`
7. **Transpuesta de una matriz/vector:** `transpose_matrix_complex(matrix)`
8. **Conjugada de una matriz/vector:** `conjugate_matrix(matrix)`
9. **Adjunta (daga) de una matriz/vector:** `adjoint_matrix(matrix)`
10. **Producto de dos matrices (de tamaños compatibles):** `mult_matrix(matrix_a, matrix_b)`
11. **"Acción" de una matriz sobre un vector:** `matrix_action_vector(matrix, vector)`
12. **Producto interno de dos vectores:** `internal_product(vector_a, vector_b)`
13. **Norma de un vector un vector:** `norm_vector(vector)`
14. **Distancia entre dos vectores:** `distance_between_vectors(vector_a, vector_b)`
15. **Valores y vectores propios de una matriz:** `eigenvalues_and_eigenvectors(matrix)`
16. **Revisar si una matriz es unitaria:** `unitary_matrix(matrix)`
17. **Revisar si una matriz es hermitiana:** `hermitian_matrix(matrix)`
18. **Producto tensor de dos vectores:** `tensor_product_vector(vector_a, vector_b)`
19. **Producto tensor de dos matrices:** `tensor_product_matrix(matrix_a,matrix_b)`
20. **Función para imprimir vectores y matrices de manera convencional:** `print_data(data)`

## Uso

1. Clona este repositorio en tu máquina local.
2. Abre el proyecto en PyCharm.
3. Importa el módulo de la librería en tus scripts.
4. Utiliza las funciones de para realizar operaciones con vectores y matrices complejos.

## Ejemplo de Uso

```python
import Lib_Vect_Mat_Complex as lvmc
import numpy as np

# Suma de vectores complejos
vector_1 = [complex(2, 9), complex(-1, 4)]
vector_2 = [complex(4, -5), complex(0, 8)]
result = lvmc.sum_vector_complex(vector_1, vector_2)
print("Suma :")
lvmc.print_data(result)

# "Acción de una matriz sobre un vector"
matriz = [[complex(2, 9), complex(-1, 4)],
          [complex(4, -9), complex(-5, -2)]]
vector = [complex(-8, -5), complex(-1, 1)]
result = lvmc.matrix_action_vector(matriz, vector)
print("'Accion' de una matriz sobre un vector:")
lvmc.print_data(result)
```
## Autor
**Ing. Juan Sebastian Vasquez Vega**
import numpy as np

matriz1 = np.array([[2, 4],
                    [3, 1]])

matriz2 = np.array([[1, 2],
                    [5, 3]])

print("Matriz 1:")
print(matriz1)

print("\nMatriz 2:")
print(matriz2)

suma = matriz1 + matriz2
print("\nSuma de Matriz1 + Matriz2:")
print(suma)

resta = matriz1 - matriz2
print("\nResta de Matriz1 - Matriz2:")
print(resta)

producto = np.dot(matriz1, matriz2)
print("\nProducto de Matriz1 * Matriz2:")
print(producto)

transpuesta1 = matriz1.T
transpuesta2 = matriz2.T
print("\nTranspuesta de Matriz1:")
print(transpuesta1)
print("\nTranspuesta de Matriz2:")
print(transpuesta2)



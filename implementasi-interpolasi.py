import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk interpolasi polinomial Lagrange
def lagrange_interpolation(x, y, xi):
    n = len(x)
    result = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (xi - x[j]) / (x[i] - x[j])
        result += term
    return result

# Fungsi untuk interpolasi polinomial Newton
def newton_interpolation(x, y, xi):
    n = len(x)
    coefficients = [y[0]]
    for i in range(1, n):
        coefficients.append(y[i])
        for j in range(i-1, 0, -1):
            coefficients[j] = (coefficients[j] - coefficients[j-1]) / (x[i] - x[j-1])
    result = coefficients[0]
    temp = 1.0
    for i in range(1, n):
        temp *= (xi - x[i-1])
        result += coefficients[i] * temp
    return result

# Data yang diberikan
x = [5, 10, 15, 20, 25, 30, 35, 40]
y = [40, 30, 25, 40, 18, 20, 22, 15]

# Contoh titik yang ingin diinterpolasi
xi = 2.5

# Interpolasi menggunakan metode Lagrange
lagrange_result = lagrange_interpolation(x, y, xi)
print("Interpolasi menggunakan metode Lagrange pada x =", xi, "adalah", lagrange_result)

# Interpolasi menggunakan metode Newton
newton_result = newton_interpolation(x, y, xi)
print("Interpolasi menggunakan metode Newton pada x =", xi, "adalah", newton_result)

# Visualisasi hasil
plt.scatter(x, y, color='red', label='Data Asli')
plt.plot(xi, lagrange_result, 'bo', label='Interpolasi Lagrange')
plt.plot(xi, newton_result, 'go', label='Interpolasi Newton')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolasi Polinomial Lagrange dan Newton')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Побудова графіка функції
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Метод Монте-Карло для обчислення інтеграла
def monte_carlo_integration(f, a, b, num_samples):
    x_random = np.random.uniform(a, b, num_samples)
    y_random = f(x_random)
    integral = (b - a) * np.mean(y_random)
    return integral

num_samples = 10000
mc_result = monte_carlo_integration(f, a, b, num_samples)
print(f"Інтеграл методом Монте-Карло: {mc_result}")

# Обчислення інтеграла за допомогою функції quad
result, error = spi.quad(f, a, b)
print("Інтеграл (quad):", result)
print("Абсолютна похибка:", error)

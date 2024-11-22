import matplotlib.pyplot as plt
import numpy as np

# напишем три функции
def f1(x):
    return x**2

def f2(x):
    return np.tan(x)

def f3(x):
    return 3*np.cos(2*x)

x = np.linspace(-np.pi, np.pi, 100)

# Первое окно с двумя графиками
plt.figure(1)
plt.plot(x, f1(x), label="f1(x)")
plt.plot(x, f2(x), label="f2(x)")
plt.title("Два графика")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

# Второе окно с одним графиком
plt.figure(2)
plt.plot(x, f3(x), label="f3(x)")
plt.title("Один график")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

plt.show()
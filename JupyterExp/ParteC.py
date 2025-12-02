import numpy as np
import matplotlib.pyplot as plt

# Definir el sistema
def sistema(X, Y):
    dxdt = -4*(X - Y)
    dydt =-Y
    return dxdt, dydt

# Crear malla de puntos
x = np.linspace(-2, 2, 15)
y = np.linspace(-2, 2, 15)
X, Y = np.meshgrid(x, y)

# Calcular derivadas
dxdt, dydt = sistema(X, Y)

# Normalizar para flechas de igual longitud
magnitude = np.sqrt(dxdt**2 + dydt**2)
dxdt_norm = dxdt / (magnitude + 1e-8)
dydt_norm = dydt / (magnitude + 1e-8)

# Dibujar
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, dxdt_norm, dydt_norm, color='blue', scale=20)
plt.plot(0, 0, 'ro', markersize=8, label='Punto crítico (0,0)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Diagrama de Fases')
plt.grid(True, alpha=0.3)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()
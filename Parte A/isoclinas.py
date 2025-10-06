import numpy as np
import matplotlib.pyplot as plt

# --- 1. Definir los Parámetros y la EDO ---
Ta = 70.0  # Temperatura ambiente 
k = np.log(0.5)  # Constante de enfriamiento, k = ln(0.5) [cite: 81]

def f(T):
    """Función de la pendiente (lado derecho de la EDO): dT/dt = k(T - Ta)"""
    return k * (T - Ta)

# --- 2. Definir la Malla (Grid) para el Gráfico ---

# Definimos el rango de tiempo (eje x) y temperatura (eje y)
# Usaremos un rango de temperatura relevante (cercano al ambiente hasta la temperatura al morir)
t_min, t_max = -3, 3  # Rango de tiempo en horas (incluye tiempo antes de t=0 (mediodía))
T_min, T_max = 60, 100 # Rango de temperatura en °F

# Crear puntos uniformes en ambos ejes
t = np.linspace(t_min, t_max, 20)  # 20 puntos de tiempo
T = np.linspace(T_min, T_max, 20)  # 20 puntos de temperatura

# Crear la malla 2D a partir de los vectores t y T
T_grid, t_grid = np.meshgrid(T, t)

# --- 3. Calcular la Pendiente en cada Punto de la Malla ---

# La pendiente es solo una función de T (dT/dt = f(T)).
# La componente U (dirección en t) siempre es 1 (para representar dT/dt).
U = np.ones(T_grid.shape)

# La componente V (dirección en T) es la pendiente f(T).
V = f(T_grid)

# Normalizar los vectores (U, V) para que todos tengan la misma longitud en la gráfica,
# lo que nos ayuda a enfocarnos solo en la dirección.
N = np.sqrt(U**2 + V**2)
U = U / N
V = V / N

# --- 4. Generar la Gráfica ---

plt.figure(figsize=(10, 6))

# Dibujar el campo de direcciones
# 't_grid' y 'T_grid' son las coordenadas de inicio del vector.
# 'U' y 'V' son las componentes del vector.
plt.quiver(t_grid, T_grid, U, V, color='gray', alpha=0.8)

# Dibujar la línea de equilibrio (Isoclina de pendiente 0)
plt.axhline(Ta, color='r', linestyle='--', label=f'Temperatura Ambiente (T={Ta}°F)')

# Añadir etiquetas y título
plt.title('Campo de Direcciones (Isoclinas) para la Ley de Enfriamiento de Newton')
plt.xlabel('Tiempo (t) [horas]')
plt.ylabel('Temperatura (T) [°F]')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()

# --- 5. Trazar una Solución (Opcional, pero muy útil para la interpretación) ---

# Solución analítica para la víctima (usando t=0 como mediodía, T0=80, k=ln(0.5))
T0_cuerpo = 80.0
C = T0_cuerpo - Ta
t_sol = np.linspace(t_min, t_max, 100)
T_sol = Ta + C * np.exp(k * t_sol)
plt.plot(t_sol, T_sol, color='blue', linewidth=2, label='Trayectoria del Cuerpo (t=0 en 12 P.M.)')

plt.ylim(65, 105) # Ajustar el límite y
plt.legend()
plt.show()
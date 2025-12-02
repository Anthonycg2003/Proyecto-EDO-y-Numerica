import matplotlib.pyplot as plt
import math
def euler(f, t0, y0, h, n):
    """
    Versión mínima para visualizar puntos del método de Euler
    """
    
    t = [t0]
    y = [y0]
    
    # Calcular todos los puntos
    for _ in range(n):
        t_nuevo = t[-1] + h
        y_nuevo = y[-1] + h * f(t[-1], y[-1])
        t.append(t_nuevo)
        y.append(y_nuevo)
    
    # Gráfico simple
    plt.figure(figsize=(9, 5))
    
    # Puntos
    plt.scatter(t, y, color='red', s=100, alpha=0.8, label='Puntos Euler', zorder=3)
    
    # Línea entre puntos (opcional)
    plt.plot(t, y, 'b--', alpha=0.5, linewidth=1)
    
    # Configurar gráfico
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.title(f'Método de Euler - {n} pasos, h={h}')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Mostrar coordenadas de cada punto
    for i, (ti, yi) in enumerate(zip(t, y)):
        plt.text(ti, yi + 0.05, f'({ti:.2f}, {yi:.2f})', 
                ha='center', fontsize=8)
    
    plt.show()
    
    return t, y

def euler_mejorado(f, t0, y0, h, n):
    """
    Método de Euler Mejorado - Versión compacta
    """
    t = [t0]
    y = [y0]
    
    for _ in range(n):
        t_actual = t[-1]
        y_actual = y[-1]
        
        # Predictor (Euler simple)
        predictor = y_actual + h * f(t_actual, y_actual)
        t_sig = t_actual + h
        
        # Corrector (Heun)
        y_sig = y_actual + (h/2) * (f(t_actual, y_actual) + f(t_sig, predictor))
        
        t.append(t_sig)
        y.append(y_sig)
    
    # Gráfico simple
    plt.figure(figsize=(9, 5))
    plt.scatter(t, y, color='red', s=100, label='Puntos Euler Mejorado', zorder=3)
    plt.plot(t, y, 'b-', alpha=0.7, linewidth=1.5)
    
    # Mostrar valores en puntos
    for ti, yi in zip(t, y):
        plt.text(ti, yi, f'  {yi:.3f}', va='bottom', fontsize=8)
    
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.title(f'Euler Mejorado: h={h}, {n} pasos')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()
    
    return t, y


# Definir la EDO
def edo(t, T):
    """ dT/dt = k(T-70) """
    k=math.log(0.5)
    return k*(T-70)

# Usar la función
t0, T0 = 0.0, 80
h = 0.2
n = 5

# Llamar a la función (muestra gráfico automáticamente)
puntos_t, puntos_y = euler(edo, t0, T0, h, n)
euler_mejorado(edo, t0, T0, h, n)
# O usar la versión mínima
# puntos_t, puntos_y = euler_puntos_visual(ejemplo_edo, t0, y0, h, n)
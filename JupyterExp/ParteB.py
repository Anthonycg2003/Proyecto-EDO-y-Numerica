import numpy as np
import matplotlib.pyplot as plt

# rango de mu y resolución
mu_min, mu_max = -2.0, 1.0
N = 800
mu = np.linspace(mu_min, mu_max, N)

# rama trivial u = 0 (vamos a trazarla con distinto estilo según estabilidad)
u_zero = np.zeros_like(mu)
stable_mask = mu < 0
unstable_mask = mu >= 0

# ramas no triviales: u = ±sqrt(-mu) solo para mu <= 0
mask_nontriv = mu <= 0
mu_nontriv = mu[mask_nontriv]
u_pos = np.sqrt(-mu_nontriv)
u_neg = -u_pos

# Preparar figura
plt.figure(figsize=(8, 6))
plt.title("Diagrama de bifurcación (μ / u)\nEcuación: $\\dot u = μ u + u^{3}$", fontsize=14)

# dibujar ramas
# rama trivial: estable (μ<0) como línea continua negra, inestable (μ>=0) como línea discontinua negra
plt.plot(mu[stable_mask], u_zero[stable_mask], 'k-', lw=2, label='u=0 (estable, μ<0)')
plt.plot(mu[unstable_mask], u_zero[unstable_mask], 'k--', lw=2, label='u=0 (inestable, μ≥0)')

# ramas no triviales (inestables para μ<0): usar línea roja discontinua
plt.plot(mu_nontriv, u_pos, 'r--', lw=2, label='u=+√(-μ) (inestable, μ≤0)')
plt.plot(mu_nontriv, u_neg, 'r--', lw=2, label='u=-√(-μ) (inestable, μ≤0)')

# marcar el punto de bifurcación (μ=0, u=0)
plt.scatter([0.0], [0.0], c='blue', s=60, zorder=5)
plt.annotate('Bifurcación en μ=0', xy=(0.0, 0.0), xytext=(0.05, 0.25),
             arrowprops=dict(arrowstyle='->', lw=1.0), fontsize=10)

# mejorar estética
plt.xlabel(r'$\mu$', fontsize=12)
plt.ylabel(r'$u$', fontsize=12)
plt.axvline(0, color='gray', lw=0.8, zorder=0)
plt.axhline(0, color='gray', lw=0.6, zorder=0)
plt.xlim(mu_min, mu_max)
plt.ylim(-1.6, 1.6)
plt.grid(alpha=0.3)
plt.legend(loc='upper right', fontsize=9)

# Añadir una pequeña explicación en la figura
texto = ("Subcrítico: la rama no trivial aparece para μ≤0\n"
         "y es inestable; u=0 cambia su estabilidad en μ=0.")
plt.gcf().text(0.02, 0.02, texto, fontsize=9)

# guardar y mostrar
plt.tight_layout()
plt.show()
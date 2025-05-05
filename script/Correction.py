"""
Correction.py

Ces scripts implémentent un modèle épidémiologique SIRD (Susceptible-Infected-Recovered-Dead) 
avec vaccination pour simuler la propagation d'une maladie infectieuse dans une population.

Le modèle utilise les équations différentielles suivantes:
dS/dt = -β*S*I/N - α*S  (Susceptibles)
dI/dt = β*S*I/N - λ*I   (Infectés)
dR/dt = λ*I             (Rétablis)
dV/dt = α*S             (Vaccinés)

où:
- N est la taille de la population
- β est le taux de transmission
- λ est le taux de guérison
- α est le taux de vaccination
"""

#%%
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Paramètres
N = 1000
β = 0.4
λ = 0.05
α = 0.02
t_final = 150

# Système SIRD + vaccination
def deriv(t, y):
    S, I, R, V = y
    dS = -β * S * I / N - α * S
    dI = β * S * I / N - λ * I
    dR = λ * I
    dV = α * S
    return [dS, dI, dR, dV]

# Conditions initiales
y0 = [999, 1, 0, 0]
t_eval = np.linspace(0, t_final, 1000)

# Résolution numérique
sol = solve_ivp(deriv, [0, t_final], y0, t_eval=t_eval, method='RK45')

# Calcul du temps où R+V atteint 75% de N
RV = sol.y[2] + sol.y[3]
t_star = np.interp(0.75*N, RV, sol.t)

# Tracé
plt.figure(figsize=(8,5))
plt.plot(sol.t, sol.y[0], label='Susceptibles')
plt.plot(sol.t, sol.y[1], label='Infectieux')
plt.plot(sol.t, sol.y[2], label='Rétablis')
plt.plot(sol.t, sol.y[3], label='Vaccinés')
plt.axvline(t_star, linestyle='--', label=f'75% immunisés à t={t_star:.1f} j')
plt.xlabel('Temps (jours)')
plt.ylabel('Nombre d’individus')
plt.legend()
plt.title('Modèle SIRD avec vaccination')
plt.grid(True)
plt.show()
# %%


import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Paramètres
beta, lambda_, alpha = 0.4, 0.05, 0.02
N = 1000
S0, I0, R0, V0 = 999, 1, 0, 0
t_span = (0, 150)

# Système d'équations
def deriv(t, y):
    S, I, R, V = y
    dSdt = - (beta * S * I) / N - alpha * S
    dIdt = (beta * S * I) / N - lambda_ * I
    dRdt = lambda_ * I
    dVdt = alpha * S
    return [dSdt, dIdt, dRdt, dVdt]

# Résolution avec RK45 (adaptive RK4)
sol = solve_ivp(deriv, t_span, [S0, I0, R0, V0], t_eval=np.linspace(0, 150, 1000))
t = sol.t
S, I, R, V = sol.y

# Calcul du seuil de 75%
V_plus_R = V + R
seuil = 0.75 * N
temps_seuil = t[np.where(V_plus_R >= seuil)[0][0]]

# Graphique
plt.figure(figsize=(10, 6))
plt.plot(t, S, label='Susceptibles')
plt.plot(t, I, label='Infectieux', color='red')
plt.plot(t, R, label='Rétablis', color='green')
plt.plot(t, V, label='Vaccinés', color='purple')
plt.axvline(temps_seuil, color='k', linestyle='--', label=f'75% atteint à t = {temps_seuil:.1f} jours')
plt.xlabel('Temps (jours)')
plt.ylabel('Population')
plt.title('Dynamique SIRD avec vaccination')
plt.legend()
plt.grid(True)
plt.show()

# %%

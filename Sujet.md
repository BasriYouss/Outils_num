---
title: "Outils numériques - Sujet"
author: "RAHARIJAONA Miahy, YOUSSOUFFOU Basri"
output:
  html_document:
    toc: true
    toc_float: true
    theme: united
---

# Dynamique épidémiologique avec vaccination : Modèle SIRD

## Problème
Résoudre le système SIRD avec vaccination et déterminer le moment où **75% de la population est vaccinée ou rétablie**.

### Modèle mathématique
- **Équations** :
  $$
  \begin{cases}
  \frac{dS}{dt} = -\frac{\beta S I}{N} - \alpha S \\[10pt]
  
  \frac{dI}{dt} = \frac{\beta S I}{N} - \lambda I \\[10pt]
  
  \frac{dR}{dt} = \lambda I \\[10pt]
  
  \frac{dV}{dt} = \alpha S 
  \end{cases}$$
  
- **Paramètres** :
  - $\beta = 0.4$, $\lambda = 0.05$, $\alpha = 0.02$
  - $N = 1000$, $I_0 = 1$, $t_{\text{final}} = 150$ jours.
## Méthode numérique
- **Choix** : Méthode de Runge-Kutta d'ordre 4 (RK4).
- **Justification** :
  - Précision élevée pour les systèmes d'équations différentielles non linéaires.
  - Adaptée aux problèmes de dynamique épidémiologique avec variations rapides.

## Résultats

### Code Python
```python
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

# Sujet 6 : Dynamique épidémiologique avec vaccination

## 1. Introduction

Ce document présente la résolution numérique d'un modèle SIRD étendu à la vaccination. On cherche à étudier l'évolution temporelle des populations :
- **Susceptibles** : S(t)  
- **Infectieux** : I(t)  
- **Rétablis** : R(t)  
- **Vaccinés** : V(t)  

Le modèle s'appuie sur le système d'équations différentielles suivant :

dS/dt = -β*S*I/N - α*S
dI/dt = β*S*I/N - λ*I
dR/dt = λ*I
dV/dt = α*S

## 2. Paramètres et conditions initiales

- Taille de la population : N = 1000  
- Taux de transmission : β = 0.4  
- Taux de guérison : λ = 0.05  
- Vitesse de vaccination : α = 0.02  

Conditions initiales :
I(0) = 1
R(0) = 0 
V(0) = 0
S(0) = N - I(0) - R(0) - V(0) = 999

Horizon de simulation : tf = 150 jours.

## 3. Méthode numérique

1. **Choix de la discrétisation**  
  - On utilisera la méthode de Runge–Kutta d'ordre 4 (RK4) ou la routine `solve_ivp` de SciPy avec le schéma « RK45 ».
2. **Implémentation**  
  - Définir une fonction Python `deriv(t, y, β, λ, α, N)` qui renvoie (dS/dt, dI/dt, dR/dt, dV/dt).
  - Appeler `solve_ivp` sur l'intervalle [0,tf] avec les conditions initiales.
  - Choisir un pas de temps adapté (ex. `t_eval = np.linspace(0, 150, 1000)`).

## 4. Résultats numériques

1. **Courbes temporelles**  
  - Tracer S(t), I(t), R(t) et V(t) sur un même graphe.
2. **Seuil de 75 % immunisés**  
  - On considère que 75 % de la population initiale est protégée dès que R(t) + V(t) ≥ 0,75*N.
  - Déterminer (par interpolation) le temps t* tel que R(t*) + V(t*) = 750.

## 5. Analyse et interprétation

- **(1) Discrétisation et justification**  
 - Comparer RK4 et RK45 (précision, coût CPU, stabilité).
- **(2) Interprétation physique**  
 - Expliquer l'impact de la vaccination sur la courbe épidémique (pic infectieux, durée de l'épidémie).
 - Analyser le temps t* et sa signification en termes de politique sanitaire.
- **(3) Qualité de la présentation**  
 - Choix des couleurs, légende, titres, annotations.
 - Clarté des axes et des unités (jours, nombre d'individus).

## 6. Graphique attendu

```python
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

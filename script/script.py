# @ Auteur: Basri, Miahy
# @ Crée le : 05/05/2025 13:54:25
# @ Description: fichier de script pour le projet en outils numériques

#%%

# Importation des modules
import numpy as np
import matplotlib.pyplot as plt
import os

# chemin pour images générées
path = os.pardir + "/img/"
os.makedirs(path, exist_ok=True)

# définition des variables
N = 1000 # population totale
I0 = 1 # personnes infectées
R0 = 0 # personnes rétablis
V0 = 0 # personnes vaccinées
tf = 150 #jours
S0 = N - I0 - R0 - V0 # personnes susceptibles
β = 0.4 # taux de contact
γ = 0.05 # taux de rétablissement
α = 0.02 # taux de vaccination
dt = 0.1 # pas de temps

# tableaux
t = np.arange(0, tf+1, dt) # temps
S = np.zeros(len(t)) # personnes susceptibles
I = np.zeros(len(t)) # personnes infectées
R = np.zeros(len(t)) # personnes rétablies
V = np.zeros(len(t)) # personnes vaccinées

# conditions initiales
I[0] = I0
R[0] = R0
S[0] = S0
V[0] = V0

# fonctions
for i in range(len(t)-1): # pour chaque rang de temps
    dS = -β*S[i]*I[i]/N - α*S[i] # variation de S
    dI = β*S[i]*I[i]/N - γ*I[i] # variation de I
    dR = γ*I[i] # variation de R
    dV = α*S[i] # variation de V
    # calcul des valeurs au rang suivant
    S[i+1] = S[i] + dS * dt 
    I[i+1] = I[i] + dI * dt
    R[i+1] = R[i] + dR * dt
    V[i+1] = V[i] + dV * dt
  

# calcul du temps où 75% de la population est vaccinée ou rétablie
X = V + R # population vaccinée ou rétablie
Y = np.abs(X - 0.75*N).argmin() # temps où 75% de la population est vaccinée ou rétablie

#affichage 
plt.figure(figsize=[10,6])
plt.plot(t, S, label='S (t) : personnes susceptibles', c = 'dodgerblue')
plt.plot(t, I, label='I (t) : personnes infectées', c = 'red')
plt.plot(t, R, label='R (t) : personnes rétablies', c = 'forestgreen')
plt.plot(t, V, label='V (t) : personnes vaccinées', c = 'fuchsia')
plt.xlabel('temps en jours')
plt.ylabel('population')
plt.axvline(t[Y], color='grey', linestyle='--', label=f'75% atteint à t = {t[Y]:.1f} jours')
plt.title('Modèle SIRV')
plt.legend()
plt.grid(ls='dashed')
plt.tight_layout()
plt.savefig(path + 'SIRV.png', dpi = 300)
plt.show()

print(f"📍 75% de la population est vaccinée ou rétablie après environ {t[Y]:.1f} jours.")



# %%

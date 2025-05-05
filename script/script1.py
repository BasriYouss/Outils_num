# @ Auteur: Basri, Miahy
# @ Crée le : 05/05/2025 13:54:25
# @ Description: fichier de script pour le projet en outils numériques

#%%

# Importation des modules
import numpy as np
import matplotlib.pyplot as plt

# définition des variables
N = 1000 # population totale
I0 = 1 #personnes infectées
R0 = 0 #personnes rétablis
V0 = 0 #personnes vaccinées
tf = 150 #jours
S0 = N - I0 - R0 - V0 #personnes susceptibles
β = 0.4 #taux de contact
γ = 0.05 #taux de rétablissement
α = 0.02 #taux de vaccination

# tableaux
t = np.arange(0, tf+1, 0.1) #temps
S = np.zeros(len(t)) #personnes susceptibles
I = np.zeros(len(t)) #personnes infectées
R = np.zeros(len(t)) #personnes rétablies
V = np.zeros(len(t)) #personnes vaccinées

# conditions initiales
I[0] = I0
R[0] = R0
S[0] = S0
V[0] = V0

# fonctions
for i in range(len(t)-1):
    dS = -β*S[i]*I[i]/N - α*S[i] #variation de S
    dI = β*S[i]*I[i]/N - γ*I[i] #variation de I
    dR = γ*I[i] #variation de R
    dV = α*S[i] #variation de V
    #calcul des valeurs au rang suivant
    S[i+1] = S[i] + dS * 0.1 
    I[i+1] = I[i] + dI * 0.1
    R[i+1] = R[i] + dR * 0.1
    V[i+1] = V[i] + dV * 0.1

#calcul du temps où 75% de la population est vaccinée ou rétablie
X = V + R #population vaccinée ou rétablie
Y = np.abs(X - 0.75*N).argmin() #temps où 75% de la population est vaccinée ou rétablie

#affichage 
plt.figure(figsize=[10,6])
plt.plot(t, S, label='S t) : personnes susceptibles')
plt.plot(t, I, label='I (t) : personnes infectées')
plt.plot(t, R, label='R (t) : personnes rétablies')
plt.plot(t, V, label='V (t) : personnes vaccinées')
plt.xlabel('temps en jours')
plt.ylabel('population')
plt.axvline(t[Y], color='k', linestyle='--', label=f'75% atteint à t = {t[Y]:.1f} jours')
plt.title('Modèle SIRV')
plt.legend()
plt.grid(ls='dashed')
plt.show()


# %%

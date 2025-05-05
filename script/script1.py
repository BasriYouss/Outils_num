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
I = np.array([I0]) #personnes infectées
R = np.array([R0]) #personnes rétablies
S = np.array([S0]) #personnes susceptibles
V = np.array([V0]) #personnes vaccinées
t = np.arange(0,tf+1,1) #temps

#variations
for i in range(len(t)):
    dS = -β*S[i]*I[i]/N - α*S[i] #variation de S
    dI = β*S[i]*I[i]/N - γ*I #variation de I
    dR = γ*I[i] #variation de R
    dV = α*S[i] #variation de V
    for j in range(len(t)-1):
        S[j+1] = S[j] + dS
        I[j+1] = I[j] + dI
        R[j+1] = R[j] + dR
        V[j+1] = V[j] + dV

#affichage 
plt.plot(t,S,label='S')
plt.plot(t,I,label='I')
plt.plot(t,R,label='R')
plt.plot(t,V,label='V')
plt.xlabel('temps')
plt.ylabel('population')
plt.title('Modèle SIRD')
plt.legend()
plt.grid(ls='dashed')
plt.show()


# %%

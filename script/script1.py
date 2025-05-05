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
I = np.zeros(tf+1) #personnes infectées
R = np.zeros(tf+1) #personnes rétablies
S = np.zeros(tf+1) #personnes susceptibles
V = np.zeros(tf+1) #personnes vaccinées
t = np.arange(0,tf+1,1) #temps

# conditions initiales
I[0] = I0
R[0] = R0
S[0] = S0
V[0] = V0

#variations
for i in range(tf):
    dS = -β*S[i]*I[i]/N - α*S[i] #variation de S
    dI = β*S[i]*I[i]/N - γ*I[i] #variation de I
    dR = γ*I[i] #variation de R
    dV = α*S[i] #variation de V
    
    S[i+1] = S[i] + dS
    I[i+1] = I[i] + dI
    R[i+1] = R[i] + dR
    V[i+1] = V[i] + dV

#affichage 
plt.figure()
plt.plot(t,S,label='S')
plt.plot(t,I,label='I')
plt.plot(t,R,label='R')
plt.plot(t,V,label='V')
plt.xlabel('temps')
plt.ylabel('population')
plt.title('Modèle SIRV')
plt.legend()
plt.grid(ls='dashed')
plt.show()

# %%

# Explication du script

Ce script modélise la propagation d'une maladie dans une population en utilisant un modèle mathématique appelé le modèle SIRV. Il simule comment le nombre de personnes susceptibles, infectées, rétablies et vaccinées évolue au fil du temps, puis affiche ces résultats sous forme de graphique.

---

## Début du script

```python
# @ Auteur: Basri, Miahy
# @ Crée le : 05/05/2025 13:54:25
# @ Description: fichier de script pour le projet en outils numériques
```

Ce sont des commentaires qui indiquent qui a écrit le code, la date de création, et une brève description.

---

## Importation des modules

```python
import numpy as np
import matplotlib.pyplot as plt
```

On importe deux bibliothèques : `numpy` pour faire des calculs avec des tableaux, et `matplotlib.pyplot` pour créer des graphiques.

---

## Définition des variables

```python
N = 1000 # population totale
I0 = 1 # personnes infectées au début
R0 = 0 # personnes rétablies au début
V0 = 0 # personnes vaccinées au début
tf = 150 # nombre de jours pour la simulation
S0 = N - I0 - R0 - V0 # personnes susceptibles au début
β = 0.4 # taux de contact (probabilité que la maladie se transmet)
γ = 0.05 # taux de rétablissement (probabilité de guérir chaque jour)
α = 0.02 # taux de vaccination (probabilité qu'une personne se vaccine chaque jour)
```

Ces variables fixent la taille de la population, le nombre initial de personnes dans chaque groupe, la durée de la simulation, et les taux qui décrivent la transmission, la guérison et la vaccination.

---

## Création des tableaux pour stocker les résultats

```python
I = np.zeros(tf+1) # personnes infectées chaque jour
R = np.zeros(tf+1) # personnes rétablies chaque jour
S = np.zeros(tf+1) # personnes susceptibles chaque jour
V = np.zeros(tf+1) # personnes vaccinées chaque jour
t = np.arange(0, tf+1, 1) # tableau du temps (jours)
```

On prépare des listes pour enregistrer le nombre de personnes dans chaque groupe pour chaque jour.

---

## Conditions initiales

```python
I[0] = I0
R[0] = R0
S[0] = S0
V[0] = V0
```

On initialise ces listes avec le nombre de personnes au début de la simulation.

---

## Boucle de calcul pour chaque jour

```python
for i in range(tf):
    dS = -β * S[i] * I[i] / N - α * S[i] # changement du nombre de susceptibles
    dI = β * S[i] * I[i] / N - γ * I[i] # changement du nombre d'infectés
    dR = γ * I[i] # changement du nombre de rétablis
    dV = α * S[i] # changement du nombre de vaccinés
    
    S[i+1] = S[i] + dS
    I[i+1] = I[i] + dI
    R[i+1] = R[i] + dR
    V[i+1] = V[i] + dV
```

Pour chaque jour, on calcule combien de personnes deviennent susceptibles, infectées, rétablies ou vaccinées, en utilisant des formules simples. Ensuite, on met à jour le nombre dans chaque groupe pour le jour suivant.

---

## Affichage des résultats

```python
plt.figure()
plt.plot(t, S, label='S')
plt.plot(t, I, label='I')
plt.plot(t, R, label='R')
plt.plot(t, V, label='V')
plt.xlabel('temps')
plt.ylabel('population')
plt.title('Modèle SIRV')
plt.legend()
plt.grid(ls='dashed')
plt.show()
```

On crée un graphique avec quatre lignes, représentant l'évolution des groupes dans le temps. On ajoute des légendes, des étiquettes, un titre, une grille, puis on affiche le graphique.

---

## Fin du script

```python
# %%
```

Ceci indique la fin ou une section du script dans certains environnements.

---

## Résumé

Ce script simule la propagation d'une maladie dans une population en utilisant des calculs simples, puis affiche un graphique pour visualiser comment le nombre de personnes infectées, rétablies, susceptibles et vaccinées évolue au fil du temps. Il permet de mieux comprendre l'évolution d'une épidémie et l'effet de la vaccination.

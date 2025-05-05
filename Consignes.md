# SUJET 6 : Dynamique épidémiologique avec vaccination

Le modèle SIRD est un modèle mathématique épidémiologique utilisé pour décrire la propagation d'une maladie infectieuse dans une population.  
Les personnes non infectées mais risquant d'être contaminées sont appelées les susceptibles, notées S(t).  
Les personnes actuellement malades et infectieuses sont appelées infectieux, notées I(t).  
Les personnes guéries après avoir été malades sont appelées les rétablis, notés R(t).  
Finalement, les personnes pouvant se faire vacciner sont appelées les vaccinés, notés V(t).

La dynamique de l'épidémie suit le système d'équation suivant :  

$\dfrac{dS}{dt} = - \beta \dfrac{SI}{N} - \alpha S \\$

$\dfrac{dI}{dt} = \beta \dfrac{SI}{N} - \lambda I \\$

$\dfrac{dR}{dt} = \lambda I \\$

$\dfrac{dV}{dt} = \alpha S$



avec :  
- \($\beta$ = 0.4\) (taux de transmission)  
- \($\lambda$ = 0.05\) (taux de guérison)  
- \($\alpha$ = 0.02\) (vitesse de vaccination)  
- \(N = 1000\) (population totale)

### Conditions initiales :  
- \($I_0$ = 1\)  
- \($R_0$ = 0\)  
- \($V_0$ = 0\)  
- \($S_0$ = N - $I_0$ - $R_0$ - $V_0$ = 999\)  
- \($t_f$ = 150\) jours

### Travail demandé :  
Résoudre le problème numériquement en utilisant une méthode numérique adaptée

### Question :  
On estime que le vaccin n'est plus nécessaire quand 75 % de la population initiale est soit vaccinée soit rétablie.  
À quel moment cela se produit-il ?

### Livrable :  
- Un graphique montrant l'évolution temporelle du nombre de susceptibles, d'infectieux, de rétablis et de vaccinés.

### Évaluation :  
Vous présenterez en 5 minutes les résultats à l'oral.  
Vous pourrez vous appuyer sur un support visuel si vous le souhaitez.  
Les critères d'évaluation sont :  
1. La discrétisation et la justification de la méthode numérique employée  
2. L'interprétation physique des graphiques obtenus  
3. La qualité de la présentation et des figures

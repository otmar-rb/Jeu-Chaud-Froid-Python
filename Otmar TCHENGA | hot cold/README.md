> TITRE : JEU CHAUD / FROID

Ceci est un jeu interactif "Chaud ou Froid" en Python où l'utilisateur doit deviner un nombre secret généré aléatoirement par l'ordinateur.
Le programme fournit aussi des indices pour aider l'utilisateur à se rapprocher du nombre secret. 

> Le jeu inclut les fonctionnalités suivantes :

# Génération aléatoire du nombre secret
# Saisie sécurisée de l'utilisateur 
# Système d'indices

# Les indices fournis sont basés sur la distance entre le nombre deviné et le nombre secret :
- "Très chaud" : Si la différence est de 1 ou 2.
- "Chaud" : Si la différence est entre 3 et 5.
- "Tiède" : Si la différence est entre 6 et 10.
- "Froid" : Si la différence est entre 11 et 20.
- "Très froid" : Si la différence est supérieure à 20.

# Limite de tentatives :

Le nombre de tentatives est calculé esn fonction de la longueur de l'interval de devinette.
Si l'utilisateur ne devine pas le nombre dans ce laps de temps, le jeu est perdu. 

# Historique des tentatives

# BDD_Devoir1
Auteur: Nicolas Corronel & Johan Maurel

## Exercice 1

Crawler (Python) + SQLite
Pre-Requis: Avoir installer Python et installer les package nécessaires
Dans le répertoire exercice1, executer le code suivant pour executer le crawler afin lancer le crawler et d'insérer les données en BDD:
```
  py getAndInject.py
```
Le crawler fait déjà un premier tri en ne choisissant que les sorts de wizard/sorcerer grâce à des RegEx. 

Résultat du programme: cf crawlerJson.png

Puis nous allons afficher à l'aide du second fichier python les sort que Pito peut faire: 
```
  py getDataInDB.py
```
Résultat (Voir ci-dessous ou capture du résultat console dans le dossier : ResultatSQLite.png)


| Nom Sort | Level | Composantes |
| ------- | -------- | ------- |
| Blindness/Deafness | 2 | V |
| Blur | 2 | V |
| Dimension Door | 4 | V |
| Feather Fall | 1 | V |
| Flare | 0 | V |
| Geas, Lesser | 4 | V |
| Knock | 2 | V |
| Shout | 4 | V |
| True Strike | 1 | V |
| Ventriloquism |  1 | V |
| Flare Burst | 1 | V |
| Steal Voice | 2 | V |
| Buoyancy | 2 | V |
| Sure Casting | 1 | V |
| Anti-Summoning Shield | 2 | V |
| Storm Ste | 3 | V |

#### Question 2: MapReduce
Sachant que chaque sort est unique, nous trouvons qu'il n'est pas pertinent d'utiliser MapReduce pour cet exercice.

## Exercice 2
Pour cet exercice, nous avons utilisé NodeJS et MongoDB donc il faut les avoir installer.
Dans le répertoire exerice2, executer le code suivant pour installer les dépendences: 

```
  npm install mongodb --save
```
Ensuite, il faut simplement lancer l'execution du JS avec la ligne :
```
  node pagerank.js
```
On peut voir qu'après plusieurs itérations, les résultats
Puis, après 20 itérations, nous obtenons les résultats attendus.
Voir capture : pagerank.png



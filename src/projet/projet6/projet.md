# Démineur

Malik et Enrico

## Motivation. 

Notre motivation pour le démineur est que c'est un jeu simple, facile à comprendre et assez plaisant à jouer.




## Introduction

Le démineur est un jeu 2D se jouant sur une grille, le but du jeu étant de découvrir chaque case sans faire exploser les mines. 




## Sources, aide, inspirations

Vidéos sur internet.
Tutoriels sur internet : - https://www.w3schools.com/python/​
- Https://docs.python.org/3/library/turtle.html



## Exemple d'une cellule Codeplay
```{codeplay}
from turtle import *

def generate(self):
        for i in range(9):
            f = randint(0, 7)
            b = randint(0, 7)
            state[f][b] = 6
            self.winlt.append(([f],[b]))
            print(self.winlt)
        self.check()

```

Ceci est la génération des bombes. Elle place aléatoirement grâce à randint 8 bombes (d'où le in range(9)).


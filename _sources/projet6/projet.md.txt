# Démineur

Malik et Enrico

## Motivation

Notre motivation pour le démineur est que c’est un jeu simple, facile à comprendre et assez plaisant à jouer.

## Introduction

Le jeu Démineur, crée dans les années 60-70, se joue sur une grille, dans laquelle sont disposées au hasard des mines. Celles-ci sont cachées derrières différentes cases de la grille. 

## But du jeu

Le but du jeu consiste donc à découvrir l'entièreté des cases ne contenant pas de mines. Pour ce faire, chacune de ces cases contient un chiffre indiquant la quantité de bombes qui se trouvent dans les carrés environnants. On peut donc ainsi placer des drapeaux sur les endroits où on suppose que des mines s'y trouvent. 

## Différentes fins possibles

Le jeu se termine soit par une défaite lorsqu'on clique sur une des cases contenant une mine, soit par une victoire lorsque toutes les cases ne contenant pas de mines ont été dévoilées. Le score se calcule grâce au temps passé à dévoiler l'entièreté des cases.

## Exemple d’une cellule Codeplay

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

Ceci est la génération des bombes. Elle place aléatoirement grâce à randint 8 bombes (d’où le in range(9)).

## Sources, aide, inspirations

Vidéos sur internet. Tutoriels sur internet : 
- https://www.w3schools.com/python/​
- Https://docs.python.org/3/library/turtle.html


# Puissance 4

Emilien

## Motivation

J'ai choisi de coder un puissance 4 car il y a la possibilité d'ajouter plein de fonctions : on peut jouer contre un joueur ou contre l'ordinateur, on peut ajouter un timer pour les joueurs, on peut créer un bouton “undo“, on peut compter le nombre de parties gagnées par joueur, etc...

Un autre aspect intéressant du puissance 4 est qu'il faut vérifier si un des joueurs a gagné, et donc vérifier (en plus des lignes et des colonnes) les diagonales. Pour l'instant cela reste un défi pour moi et j'ai hâte de me pencher sur ce problème.

De plus j'ai quelques idées, par exemple permettre au(x) joueur(s) d'entrer leur nom au début du jeu, puis ce nom changera de couleur si c'est à lui de jouer ou non, ou alors (lorsqu'un joueur a gagné) de changer l'aspect des pions gagnants (donc le programme doit connaitre les coordonnées des pions gagnants), ou encore de permettre au joueur de sélectionner dans un premier temps la colonne dans laquelle il veut jouer, puis dans un second temps de confirmer si il souhaite jouer dans cette colonne.

## Codeplay

```{codeplay}
from turtle import *

```


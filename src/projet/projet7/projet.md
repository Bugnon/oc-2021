# Puissance 4

Emilien

## Motivation

J'ai choisi de coder un puissance 4 car il y a la possibilité d'ajouter plein de fonctions : on peut jouer contre un joueur ou contre l'ordinateur, on peut ajouter un timer pour les joueurs, on peut créer un bouton “undo“, on peut compter le nombre de parties gagnées par joueur, etc...

Un autre aspect intéressant du puissance 4 est qu'il faut vérifier si un des joueurs a gagné, et donc vérifier (en plus des lignes et des colonnes) les diagonales. Pour l'instant cela reste un défi pour moi et j'ai hâte de me pencher sur ce problème.

De plus j'ai quelques idées, par exemple permettre au(x) joueur(s) d'entrer leur nom au début du jeu, puis ce nom changera de couleur si c'est à lui de jouer ou non, ou alors (lorsqu'un joueur a gagné) de changer l'aspect des pions gagnants (donc le programme doit connaitre les coordonnées des pions gagnants), ou encore de permettre au joueur de sélectionner dans un premier temps la colonne dans laquelle il veut jouer, puis dans un second temps de confirmer si il souhaite jouer dans cette colonne.

## Description du jeu

blabla

## Réprésentation de l'état

L'état du jeu est représenté avec un tableau 2D appelé ``state``

```{codeplay}
state = []

for i in range(6):
    state.append([0] *7)

for line in state:
    print(line)
```

Après deux tours, l'état pourrait se présenter ainsi:

```{codeplay}
state = []

for i in range(6):
    state.append([0] *7)

state[5][1] = 1
state[5][2] = 2
    
for line in state:
    print(line)
```

## Les variables

Formules mathématiques en LaTeX

$$ a^2 = x_2 $$

## Comment jouer

votre interface

![description](image.png)


## Codeplay

```{codeplay}
state = []

for i in range(6):
    state.append([0] *7)

for line in state:
    print(line)
```


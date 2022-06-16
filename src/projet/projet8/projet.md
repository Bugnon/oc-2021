# Othello

Arthur, 16.06.2022

## Description

Le jeu d'Othello se joue sur une grille 8 x 8

## Représentation

Le jeu est représenté avec une liste 2D par une variable ``state``.


```{codeplay}
state = []

for i in range(8):
    state.append([0] *8)

for line in state:
    print(line)
```

La signification 

- 0 : case vide
- 1 : case rempli par joueur 1 (noir)
- 2 : case rempli par joueur 2 (gris)

## Evolution

Le joueur peut cliquer dans une cellule.
Supposons qu'il clique dans la cellue de la rangée 2, colonne 3, ce qui correspond à ``state[2][3]``.

```{codeplay}
state = []

for i in range(8):
    state.append([0] *8)

state[2][3] = 1

for line in state:
    print(line)
```

## Conclusion

blabla


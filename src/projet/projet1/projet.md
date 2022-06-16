# Jeu 2048

Alice et Grégory

2048 est un jeu individuel dans lequel le but est d’arriver à 2048 en associant des puissances de 2.
Ce jeu se déroule sur un plateau 4x4 donc sur 16 cases.
Chaque tour, le joueur doit faire bouger les cases dans un des quatre sens. Les cases de même nombre s’assemblent pour former une nouvelle case qui a un nombre double que ceux d’avant. A la fin du tour, une nouvelle case, portant le nombre 2, se rajoute aléatoirement sur le plateau.

![image](https://user-images.githubusercontent.com/89935590/166827743-4511b79d-c453-41c3-bd73-c242957afa70.jpeg)

## Réprésentation de l'état
l'état du jeu est représenté avec un tableau 2d appelé state
## Codeplay

```{codeplay}
state = [
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
]

for ligne in state:
    print(ligne)

```
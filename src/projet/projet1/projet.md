# Jeu 2048

Alice et Grégory

2048 est un jeu individuel dans lequel le but est d’arriver à 2048 en associant des puissances de 2.

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
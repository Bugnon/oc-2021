# Pacman
 Les contributeurs de ce jeu sont Alex et Walid

## Motivation

Nous avons choisi Pacman car il s'agit d'un jeu mytique, un jeu des salles d'arcade et surtout intemporelle. On se devait donc de le reprendre.

## Description du jeu
Le pacman (rond jaune) doit récolter un maximum de point en évitant les fantômes (rond rouge). Notre jeu possède deux labyrinthes.  Pour accéder au nuiveau suivant, tous les points doivent être récupérés.

## Interface
Un fond noir avec un labyrinthe bleu, ce dernier est constitué de points blancs qui sont récoltés par le pacman.
Il y a deux bouttons, un quit pour quitter la partie et un autre retry pour recommencer la partie, ce dernier ne s'affiche qu'une fois apres avoir été attraper par les ghosts.

## Structure

La structure est composé de  8 classses;    - Rectangle
                                            - Text
                                            - Button
                                            - Ghost
                                            - Pacman
                                            - World
                                            - Score
                                            - Game




## Codeplay

```{codeplay}
from turtle import *
def load(self, tiles):
    """load a level"""
    self.tiles = tiles
    for i in range(20):
        for j in range(20):
            tile = tiles[i][j]
            if tile == 2:
                tiles[i][j] = 1
    self.path.clear()
    self.draw()
    self.game.pacman = Pacman(self.game, vector(-40, -80), vector(5, 0), vector(5, 0), False)
    self.game.ghost = [
        Ghost(self.game, vector(-180, 160), vector(5, 0)),
        Ghost(self.game, vector(-180, -160), vector(0, 5)),
        Ghost(self.game, vector(100, 160), vector(0, -5)),
        Ghost(self.game, vector(100, -160), vector(-5, 0)),
    ]
```


## Source
Un site qui receuil divers jeux avec python dont celui qui nous a permis d'avoir la base de notre jeu:
 https://pypi.org/project/freegames/ .

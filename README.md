# OC informatique 2021-22

## Objectif

L'objectif de ce cours est de donner une introduction à l'informatique en utilisant les outils des *pro* et des *hackers*. Nous allons nous familiariser avec

- le terminal
- les commandes UNIX
- le logiciel de gestion de version **Git**
- la plateforme GitHub
- les notebook Jupyter
- programmation en Python

## Logiciels à installer

- Thonny, un éditeur simple pour Python
- VS Code, un éditeur avancé
- GitHub Desktop, interface graphique


## Installation

    WARNING: You are using pip version 19.2.3, however version 21.2.4 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.


## Compiler le livre

Les documents pour ce site se trouvent dans le dossier `doc`. Pour créer les pages HTML allez exécutez

    cd doc
    jb build .

Pour visualiser les pages:

    open build/index.html

Pour pousser les pages vers GitHub Pages

    ghp-import -n -p -f build

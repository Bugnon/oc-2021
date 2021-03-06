# Annexe

Ce site est créé avec sphinx présenter les projets de fin d'année de la classe OC informatique. 
Le format et la structure de la page est identique au site **modulo**

Sur Github nous avons la structure

```text
src
    assets          # copié de modulo
    exts            # copié de modulo
    projet          # projets des élèves
        media       # dossier pour images
        code        # dossier pour code
        index.md    # page de départ
        projet.md   # page projet d'élève
    static          # copié de moduloe
requirements.text   # les modules Python à installer
```

Voici une image dans le dossier `media`.

![go](media/go-atari.png)


## Installation

Voici les étapes à faire chez vous 

- installer [GitHub Desktop](https://desktop.github.com) 
- installer [VS Code](https://code.visualstudio.com/download)

### VS Code

Installer les extensions

- Python extension for Visual Studio Code (de Microsoft)
- Live Server (de Ritwick Dey)

- dans la console VS Code

```text
pip3 install -r requirements.txt
```

Mettre à jour pip (package installer for Python).

```text
pip3 install --upgrade pip
```

Voici les chemins (path) cherchés lors de l'exécution d'une commande

```text
echo $PATH
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

Ajouter les extensions Python au chemin (path).

```text
export PATH=~/Library/Python/3.10/bin:$PATH
```

Pour créer les pages web dans le dossier `build``


```text
sphinx-build src/projet build -E
```

alternativement

```text
python3 -m sphinx src/projet build -E
```
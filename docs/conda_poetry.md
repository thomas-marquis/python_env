# Miniconda & poetry

## Installation

**pour windows**

- [Télécharger l'instalateur](https://docs.conda.io/en/latest/miniconda.html) et lancer l'installation
- cocher l'option add to PATH"

afficher les versions de python disponibles :

```
conda search python
```

créer un environnement virtuel avec une version spécifique de python :

```
cd ./myrepo
conda create --name py38 python=3.8.1
```

`py38` est le nom de l'environnement virtuel

Pour l'activer :

```
conda activate py38
```

**remarque pour windows** : utiliser le terminal cmd

à partir de là, on pointe vers la version 3.8.1 de python :

```
python --version
```

**pour changer de version de python**

Oups ! on a pas installé la bonne version ! En fai on veux la version 3.7

Pour ça (toujours dans l'environnement virtuel), il suffit de l'installer :

```
conda install python=3.7
python --version
```

et tant qu'a faire, on va rennomer l'environnement virtuel :

```
conda deactivate
conda create --name py37 --clone py38
conda remove --name py38 --all
conda activate py37
python --version
```

installons `poetry` :

```
conda install poetry
```

**sur windows**, vérifier qu'il n'y a pas d'autre petry installé sur le pc. Regarder par exemple dans `~/AppData/Local`, si un dossier `poetry` s'y trouve, le supprimer.

initialiser le repo :

```
poetry init --no-interaction
```

Pour vérifier que l'installation s'est bien passée :

```
poetry env info
```

et vérifier que le path pointe bien vers notre environnement miniconda `py37`

## Utilisation

on peux maintenant utiliser poetry pour installer les dépendances :

```
poetry add requests
```

la commande a mis à jour la liste des dépendances dans le fichier `pyproject.toml` et à créé un fichier `poetry.lock`

**gestion des dev dependancies**

si par exemple, on souhaite pouvoir lancer un notebook jupyter depuis notre environnement, il faut l'ajouter en dev dependancy :
````shell script
poetry add jupyter -D
````

on peut maintenant utiliser le notebook. Il aura accès à toute les dépendances du projet.
````shell script
jupyter-notebook
````

**tests unitaires**
installer et lancer pytest :

````shell script
poetry add pytest -D
pytest
````

## build et déploiement

TODO

## Intégration dans les IDE

### VScode

C'est automatique si on a l'extension python d'activée.

### Pycharm

Aller dans settings > Project > Project interpreter
ajouter un nouvel environnement, sélectionner 'conda environement' puis cocher 'existing environment'
Retrouver l'environnement virtuel py37

C'est tout !

## Bilan

### Avantages

- fonctionne super bien sur windows
- plutôt simple et rapide à utiliser (au regard des autres solutions)
- permet une gestion fine des versions de python et des dépendances (grace à poetry)
- s'intègre bien dans les IDE (grâce à conda)


## Inconvégients

RAS

# Pyenv et Poetry

- [Mettre en place son environnement](#mettre-en-place-son-environnement)
  - [Installer pyenv](#installer-pyenv)
  - [Installer python](#installer-python)
  - [Installer poetry](#installer-poetry)
- [Commencer à coder](#ecrire-un-projet)
  - [Initialiser un projet](#initialiser-un-projet)
  - [Pendant le développement](#utiliser-poetry-pandant-le-dveloppement)

## Mettre en place son environnement

**ressources**

- [une série d'article sur Medium qui explique comment configurer son environnement sans (trop) se prendre la tête](https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769)
- [installer pyenv sur windows](https://github.com/pyenv-win/pyenv-win)

On utilise deux outils géniaux : **pyenv** et **poetry**.
Ce sont les équivalent de `yarn` ou `npm` pour le js

### Installer `pyenv`

Installer python à la main, ça peux être super simple et bien se passer comme ça peux prendre des heures jusqu'à l'abandon.
`puenv` résout se problème.

**sur linux**

- [La doc de pyenv se trouve là](https://github.com/pyenv/pyenv)
- [La doc de l'installer ici](https://github.com/pyenv/pyenv-installer)

C'est facile :

```shell script
curl https://pyenv.run | bash
```

il faut ensuite ajouter `$HOME/.pyenv/bin` au path dans le fichier `~/.bashrc` pour avoir la commande `pyenv`
dispo au lancement du shell.

**sur windows**

- [la doc de pyenv-win est trouvable ici](https://github.com/pyenv-win/pyenv-win)

Il faut utiliser `pyenv-win` que l'on install à l'aide de `pip` :

```shell script
pip install pyenv-win --target %USERPROFILE%/.pyenv
```

Ca va créer un dossier `.pyenv` dans le dossier utilisateur (pas de droit admin requis).
Il faut ensuite ajouter `%USERPROFILE%/.pyenv/bin` et `%USERPROFILE%/.pyenv/shims` au `path`.

Vérifier l'installation avec une `pyenv --version` et **dans le dossier où se trouve `.pyenv`**
lancer la commande :

```shell script
pyenv rehash
```

L'installation est terminée !

### Installer python

avec `pyenv` on peux installer python tranquillement.

pour lister toutes les versions dipo :

```shell script
pyenv install -l
```

et pour installer une version :

```shell script
pyenv install 3.8.2
```

**sur windows**, après chaque installation, penser à faire un :

```shell script
pyenv rehash
```

**toujours sur windows**, il n'est pas possible d'installer une version de python avec `pyenv`
si une version plus récente est déjà installée sur le poste. Il faut d'abord la suppprimer
dans le panneau de configuration.

Par exemple, si on veux installer la version `3.8.0` avec poetry, mais que la version `3.8.2`
à déjà été installée (à la main) sur le poste, il faudra commencer par la désinstaller.

dans le dossier de notre projet, on défini quelle version de python on veux utiliser à l'aide de :

```shell script
pyenv local 3.8.2
```

il est aussi possible de définir la version de python par défaut à l'échelle du poste :

```shell script
pyenv global 3.8.2
```

on peut accéder à la version localement installée à l'aide de :

```shell script
pyenv exec python
```

### Installer `poetry`

- [La doc de poetry est trouvable ici](https://python-poetry.org/docs/)

```shell script
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

## Ecrire un projet

Dans cette partie, on va voir comment initialiser un projet, installer ses dépendances et
le lancer.

### Initialiser un projet

Dans un repo existant (par exemple, juste un dossier vide) :

```shell script
poetry init --no-interaction
```

cette commande va créer un fichier `pyproject.toml`, qui est un peu l'équivalant du
`packages.json` de node.

**sur windows**, il faut indiquer à petry quelle version de python on veux utilisé (malgré que ce
soit déjà indiqué dans le pyproject.toml...). La commande pour ça :

```shell script
poetry env use /path/to/pyenv/python
```

**penser à utiliser des `/` dans le path, et non des `\\`** !!

exemple de path : `C:/users/[username]/.pyenv/pyenv-win/versions/3.8.0/python`

lancer ensuite cette commande pour installer le projet :

```shell script
poetry install
```

### Utiliser poetry pandant le développement

pour installer une dépendance (par exemple `requests`) :

```shell script
poetry add requests
```


## Bilan

### avantages

- simple à utiliser. Poetry s'utilise comme yarn et pyenv comme nvm
- permet de choisir et d'installer automatiquement une version spécifique de python

### inconvégniants

- marche extraimement mal sur windows, et encore plus quand on n'est pas admin on quand on est derrière un firewall un peu trop violent...
- n'est pas (encore) bien intégré aux IDE, pycharm ne l'integre pas ([une issue est en cours à ce sujet](https://youtrack.jetbrains.com/issue/PY-30702))

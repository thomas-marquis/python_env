# benchmark des environnements virtuels

## virtualenv

````shell script
$ pip install virtualenv
$ virtualenv -p /usr/bin/python2.7 venv
$ source venv/bin/activate
(venv) $ pip install numpy
(venv) $ pip freeze > requirements.txt

$ pip install virtualenv
$ virtualenv -p /usr/bin/python2.7 venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
````

avantages :

- isole les dépendances
- portabilité des projets

inconvénients :

- ne gère pas l'installation de python
- génération du fichier de dépendances manuelle
- ne gère pas les tests, les builds et le déploiement
- ne sépare pas les dépendances de dev de celles de prod

## pipenv

````shell script
$ pip install pipenv
$ pipenv install numpy
````

avantages (en plus de ceux de virtualenv) :

- séparation des dev dependencies
- gère l'installation de python
- génère et maintient des fichiers de dépendance

inconvénients :

- lent



## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- `python manage.py runserver --settings=oc_lettings.settings.local`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Déploiement

### Descriptif

Lors d'un push, un pipeline CircleCI est déclenché.
  - lancment d'un build validé par flake8 et pytest

  Uniquement pour la branche main:
  - build d'un contenaire déposé sur Docker Hub
  - déploiement sur Heroku

### Suivi sur CircleCI

Cliquer sur ce [lien](https://app.circleci.com/launchpad/invited?return-to=https%3A%2F%2Fapp.circleci.com%2Fpipelines%2Fgithub%2Fjcouignoux%2FP13_couignoux_julien%3Finvite%3Dtrue&inviter=b1b54806-d869-47c0-8a45-505361518a86&invitePage=pipelines) puis connecter vous à CircleCI (ou créer un compte si nécessaire)

Pipeline CircleCi (décrit dans `.circleci/config.yml`):  
 toutes branches:
 - build_and_test: création de l'environnement puis lancement de pytest et flake8
 - cont: build d'un contenaire puis dépôt sur DockerHub  

uniquement branche main:
 - deploy: déploiement de l'environnment sur Heroku

### Conteneurisation

Aller sur Docker Hub [ici](https://hub.docker.com/repository/registry-1.docker.io/jucgx/oc-lettings-site/tags?page=1&ordering=last_updated).
Vérifier que le conteneur a bien été déposé (le tag correspond au commit CircleCI) ainsi que le latest qui doit avoir un DIGEST identique.

Tester le conteneur en local
 - Lancer la commande docker-compose up. Celui-ci récupère l'image taguée `latest` puis lance l'application.
 - Connectez-vous sur le port [8090](http://localhost:8090/).

### Déploiement Heroku

Lancement déploiement:
 - Le déploiement se fait automatiquement en mettant à jour la branche main.
 - Relancer le workflow d'une brach main depuis CircleCI


> Attention ! Pour le premier déploiement, la base de donnée sera vide. Un backup de la base a été exportée dans /oc_lettings/dumps/db.json.  
Il faut donc recharger la base avec la commande `python manage.py loaddata ./oc_lettings/dumps/db.json`.
> - Depuis le dashbord Heroku de l'application - More - Run console
> - Depuis le cli Heroku (installation [ici](https://devcenter.heroku.com/articles/heroku-cli))
> 1. `heroku login`
> 2. `heroku run --app <app_name> python manage.py loaddata ./oc_lettings/dumps/db.json`


Se connecter sur Heroku [https://oc-lettings-site-jc.herokuapp.com/](https://oc-lettings-site-jc.herokuapp.com/)


### Sentry

Suivi sur [Sentry](https://sentry.io/organizations/cgx/projects/oc_letting_site/?project=4504003434250240).
Seules les alertes en environnment de production sont remontées.

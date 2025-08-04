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

#### Initialiser les variables d'environnement

- Créer le fichier `.env` à la racine du projet
- Ajouter les variables d'environnement suivantes :

  ```
  DEBUG=False
  SECRET_KEY=your_secret_key
  SENTRY_DSN=https://<publicKey>@o0.ingest.sentry.io/<projectID>
  ```

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
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

## Pipeline CI/CD et Déploiement

### Vue d'ensemble

Le projet utilise un pipeline CI/CD automatisé avec GitHub Actions qui s'exécute à chaque push sur la branche `main`. Le pipeline est composé de deux étapes principales :

1. **Tests et validation** : Exécution des tests unitaires, vérification du linting et de la couverture de code (>= 80%).

2. **Déploiement** : Construction de l'image Docker, publication sur Docker Hub et déploiement sur Render.

### Configuration requise

- Un compte [Docker Hub](https://hub.docker.com/) pour héberger les images
- Un compte [Render](https://render.com/) pour l'hébergement
- Les secrets suivants configurés dans les paramètres GitHub de votre dépôt :
  - `DOCKERHUB_USERNAME` : Votre nom d'utilisateur Docker Hub
  - `DOCKERHUB_TOKEN` : Votre token d'accès Docker Hub
  - `RENDER_DEPLOY_HOOK_URL` : L'URL du webhook de déploiement Render

### Variables d'environnement Render

Les variables suivantes doivent être configurées dans le tableau de bord Render :

- `ALLOWED_HOSTS` : "oc-lettings-latest-qgxn.onrender.com, oc-lettings.onrender.com"
- `DEBUG` : "False"
- `SECRET_KEY` : Votre clé secrète Django
- `SENTRY_DSN` : Votre DSN Sentry pour la surveillance des erreurs

### Étapes de déploiement

1. Configurez les secrets dans les paramètres GitHub de votre dépôt
2. Configurez les variables d'environnement dans le tableau de bord Render
3. Poussez vos modifications sur la branche `main` pour déclencher le pipeline

### Workflow CI/CD

Le pipeline est défini dans [.github/workflows/ci-cd.yml](.github/workflows/ci-cd.yml) et comprend :

1. **Tests et validation** (sur chaque push et PR)

   - Installation des dépendances
   - Vérification du style avec flake8
   - Exécution des tests unitaires avec une couverture minimale de 80%

2. **Publication de l'image Docker** (uniquement sur `main`)

   - Construction de l'image Docker
   - Publication sur Docker Hub avec les tags :
     - `latest` pour la dernière version stable
     - `[commit-hash]` pour la traçabilité

3. **Déploiement sur Render** (uniquement sur `main`)
   - Déclenchement via webhook
   - Redémarrage automatique du service
   - Accès à l'application : [https://oc-lettings-latest-qgxn.onrender.com](https://oc-lettings-latest-qgxn.onrender.com)

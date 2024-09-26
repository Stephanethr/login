# Projet de Système de Login avec Django

## Description

Ce projet est un système de login simple développé avec Django. Il permet aux utilisateurs de s'enregistrer, de se connecter et de visualiser une page d'accueil après leur authentification. Le système utilise une base de données pour stocker les informations des utilisateurs.

## Technologies Utilisées

- **Python** : Langage de programmation principal.
- **Django** : Framework web pour construire l'application.
- **SQLite** : Base de données par défaut utilisée pour stocker les informations des utilisateurs.
- **HTML/CSS** : Pour le développement de l'interface utilisateur.

## Fonctionnalités

- **Inscription** : Permet aux utilisateurs de créer un nouveau compte.
- **Connexion** : Permet aux utilisateurs d'accéder à leur compte.
- **Page d'accueil** : Page d'accueil affichée après la connexion réussie.
- **Gestion des erreurs** : Gère les erreurs d'authentification et d'inscription.

## Installation

### Prérequis

- Python 3.x
- Django 5.x

### Étapes d'installation

1. **Cloner le dépôt** :
   ```bash
   git clone <url_du_dépôt>
   cd login

### Créer un environnement virtuel :

```
python -m venv .venv
```

## Activer l'environnement virtuel :

### Sur Windows :

```
.venv\Scripts\activate
```

### Sur macOS/Linux :

```
source .venv/bin/activate
```

### Installer les dépendances :

```
pip install django
```

### Configurer la base de données : Exécuter les migrations pour créer les tables nécessaires dans la base de données :

```
python manage.py migrate
```

### Lancer le serveur de développement :

```
    python manage.py runserver

    Accédez à l'application via http://127.0.0.1:8000.
```

## Structure du Projet

login/
    ├── accounts/
    │   ├── migrations/
    │   ├── static/
    │   │   └── accounts/
    │   │       ├── css/
    │   │       └── images/
    │   ├── templates/
    │   │   └── accounts/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── login/
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    └── README.md


# Les images de background
    - url : app/app/static/js/main.js   -> changer les images slide1, 2 ...

# Configuration Email
    - EMAIL_HOST = '********************' -> le chager avec le smtp de ton server
    - EMAIL_FROM = '********************' -> le changer avec le mail professionnel
    - EMAIL_HOST_USER = '********************' -> le même mail
    - EMAIL_HOST_PASSWORD = '********************' -> le changer avec le mot de passe email
    - EMAIL_PORT -> Depand du server que tu utilises

# Identifiants De connexion Admin
    - url local : 127.0.0.1:8000/admin
    - user : admin-oc
    - password : password-oc

# Environnement de developpement && de production
    - url de developpement : app/app/settings/dev.py
    - url de production : app/app/settings/prod.py

# Changer ceci : app.settings.dev
    - dans le fichier : app/app/wsgi.py
    - dans le fichier : app/app/asgi.py

# Commande d'installation des dépendances
    - dans le dossier app depuis la racinne après avos
    - pip install -r requirements.txt

# Lancer le server
    - python manage.py runserver
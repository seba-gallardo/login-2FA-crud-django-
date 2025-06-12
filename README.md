# login-crud-django

### Comandos Django
- django-admin startproject mi_proyecto
- python manage.py runserver
- python manage.py startapp mi_app
- python manage.py createsuperuser
- python manage.py makemigrations
- python manage.py migrate

### Comandos Miniconda (Entorno virtual)
- conda create --name mi_entorno python=3.12.9
- conda activate mi_entorno
- conda list
- conda env list

### Comandos generales
- pip install -r requirements.txt
- pip install django

### Eliminar migraciones
1. del db.sqlite3
2. del mi_app\migrations\0*.py
3. python manage.py makemigrations
3. python manage.py migrate
5. python manage.py createsuperuser

### Cargar branch
1. git fetch
2. git checkout nombre_branch
3. git branch -a (Lista todas las ramas disponibles)

### Branch
- git branch                 # Lista ramas locales
- git branch nueva-rama      # Crea una nueva rama
- git checkout nueva-rama    # Cambia a esa rama
- git checkout -b rama       # Crea y cambia a la rama
- git merge otra-rama        # Fusiona otra-rama con la actual

### Comandos git
- git init
- git clone URL
- git status 
- git add .
- git add archivo.txt  
- git commit -m "Mensaje"
- git pull origin main(branch)
- git push origin main(branch)
- git rm archivo.txt               # Elimina archivo del repo
- git checkout -- archivo.txt      # Deshace cambios en un archivo
- git reset --soft HEAD~1          # Quita el último commit, pero deja los cambios
- git revert id_commit             # Crea un commit que revierte uno anterior

### Configuracion inicial git
- git config --global user.name "Tu Nombre"
- git config --global user.email "tucorreo@example.com"

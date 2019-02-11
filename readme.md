# How to run: (this is assuming a current ubuntu install, windows may be tricker but google around)
* download the repository
* pip install virtualenv
* cd into the repository
* run python3 -m virtualenv env
* run source env/bin/activate
* run pip install -r requirements.txt
* setup your postgress server (this one is kinda tricky but here is a good guide https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)
* create a role on the postgress server that is a superuser
* change the settings file in django-example/example/example/settings.py (i'm learning :( ) to reflect your database user
* create a database caled example on the postgress server
* run cd example (so that your path is django-example/example)
* run python3 manage.py makemigrations
* run python3 manage.py migrate
* run python3 manage.py runserver

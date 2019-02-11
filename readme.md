# How to run:
**This is assuming a current ubuntu install, windows may be tricker but google around**
* download the repository
  * sudo apt install git
  * Press Y when prompted
  * run git clone https://github.com/rocke97/ExampleCapstoneDjangoAPI.git
* run cd ExampleCapstoneDjangoAPI
* run sudo apt install python3-pip
  * Press Y when prompted
* run pip3 install virtualenv
* run python3 -m virtualenv env
* setup postgres server
  * run sudu apt update
  * run sudo apt install postgresql postgresql-contrib
  * if the name of your linux login isn't just your first name run sudo adduser <firstNameHere>
  * run sudo -u postgres createuser --interactive
    * For "name of the role to add" use your first name
    * For if it should be a super user hit y
  * run sudo -u postgres createdb <firstNameHere>
  * run sudo -u postgres createdb example
  * run sudu -u <firstNameHere> psql
  * run \password
  * enter a password here and remember it for later
  * run \q
* run source env/bin/activate
* run pip3 install -r requirements.txt
* open the settings file in django-example/example/example/settings.py (i'm learning :( )
* under DATABASES in the file
  * change the USER entry to your first name
  * change the PASSWORD entry to the password you entered after running \password
* run cd .. (so that your path is django-example/example)
* run python3 manage.py makemigrations
* run python3 manage.py migrate
* run python3 manage.py runserver **you need to leave this terminal open for the server to run**
* go to http://localhost:8000/api/v1/users/ to see the get and post users endpoint
* you can add users to your database from this page

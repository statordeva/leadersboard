# Leaders Board Challenge

## Admin
superuser is `admin admin@mail.com admin123`

## How to run
- activate env `source newenv/bin/activate`
- seed users `./manage.py usersseed 5`
- run server `./manage.py runserver`
- run scheduled task `./manage.py runapscheduler`
- open `http://localhost:8000/board/`
- run tests `./manage.py test`

## Setup Virtual Env
- install `sudo pip install virtualenv`
- go to folder `mkdir ~/newproject && cd ~/newproject`
- create venv `virtualenv newenv`
- activate venv `source newenv/bin/activate`
- install django `pip install django`
- check django `django-admin --version`
- leave your virtual environment `deactivate`
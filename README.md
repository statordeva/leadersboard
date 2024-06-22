# Leaders Board Challenge

## Admin
superuser is `admin admin@mail.com admin123`

## How to run
- activate env `source newenv/bin/activate`
- install dependencies `pip install -r requirements.txt`
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
- leave your virtual environment `deactivate`
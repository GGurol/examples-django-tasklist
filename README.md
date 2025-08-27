!!! Notice !!!
This project forked from https://github.com/memcachier/examples-django-tasklist

The project was originally written for Python 2.7 and Django 2.1. The code has been upgraded for Python 3.12 and Django 4.2, and external resources have been localized.



# MemCachier and Django tutorial

This is an example Django~=4.2 task list app that
uses the [MemCachier add-on](https://addons.heroku.com/memcachier) on
[Heroku](http://www.heroku.com/). 



## Running Locally

Run the following commands to get started running this app locally:


on docker:
```sh
$ git clone https://github.com/GGurol/examples-django-tasklist.git
$ cd examples-django-tasklist
$ docker compose up --build
```

on another terminal session:
```sh
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```


on virtual environment:
```sh
$ git clone https://github.com/GGurol/examples-django-tasklist.git
$ cd examples-django-tasklist
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

Then visit `http://localhost:8002` to play with the app.


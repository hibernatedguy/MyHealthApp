# MyHealthApp

myhealthapp : Health App written in flask with postgreSQL.


# Project Structure
```
myhealthapp
├── README.md
├── __pycache__
├── applications
│   ├── __init__.py
│   ├── __pycache__
│   ├── checkups
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── models.py
│   │   ├── serializers.py
│   │   └── views.py
│   ├── common
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── decorators.py
│   │   └── models.py
│   ├── profiles
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── models.py
│   │   ├── serializers.py
│   │   └── views.py
│   └── rest_auth
│       ├── __init__.py
│       ├── __pycache__
│       └── rest_auth.py
├── celerybeat-schedule.db
├── celerybeat.pid
├── checkup_log.json
├── config
│   ├── __init__.py
│   ├── __pycache__
│   ├── flask_celery.py
│   ├── secrets.json
│   └── settings.py
├── docs
│   └── Health\ APIs.postman_collection.json
├── manage.py
├── migrations
├── reporting_tasks.py
├── requirements.txt
└── tests
    ├── __init__.py
    └── test_flaskr.py
```

> applications/* folder contains pluggable apps, which can be re used in some other projects
> applications/<app_name>/models.py contains db-model structure
> applications/<app_name>/views.py contains ClassBasedViews to handle HTTP requests
> docs/* holds all documentation related stuff
> manage.py subcommands to execute multiple tasks like, runserver, runtests, migratedb etc.
> requirements.txt contains package information
> config/ folder contains all configuration and secrets of project
> tests/ folder contains all test cases.
> reporting_tasks.py to run celery job in background

# Create database
```
psql -U postgres -c "create database development_db"
psql -U postgres -c "create database testing_db"
```
or 
```
createdb development_db
createdb testing_db
```

# Install packages
pip install -r requirements.txt

# App run and db setup
```
python manage.py runserver
```

# Testing
```
py.test or pytest
```

# API Doc
[POSTMAN Doc](https://documenter.getpostman.com/view/227044/RzfassBD)

# Postman Collection
visit **docs/** directory

# Celery
To start the Celery workers, you need both a Celery worker and a Beat instance running in parallel. Here are the commands for running them:

celery -A manage.celery worker --loglevel=info
celery beat -A manage.celery --loglevel=info

* please make sure redis-server is running in background

# Send reports to reporting-server
- Using simple python-request module.
- By using celery worker sending reports to reports-server.
- Since it's a background task so always there will be 2 calls, 
    - 1 reading reports form database
    - 2 read/write sync date to database
- By using file based logging system there will be only one api call for read reports.
- If in future we are removing this service, there will be no useless loggin-data in database.

# Authentication
- Token based authentication on CheckupsAPI

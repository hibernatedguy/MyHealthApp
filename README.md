# MyHealthApp

HealthApp : Yet another flask app with RESTAPIs 

Fictitious health-care startup that does health checks for multiple connected instruments. The instruments currently save results via mobile client when all check-ups are done, it does the bulk upload reports.

Organziation is having a trouble with querying it's single source of truth database ( postgreSQL) and need to transforming and migrating user reports data to separate database ( NoSQL ) on periodic basis to store and serve user report data via mobile client.


# Project Structure
```
├── LICENSE
├── README.md
├── docs
│   ├── postman-api-collections
│   └── postman-api-docs
├── myhealthapp
│   ├── applications
│   │   ├── __init__.py
│   │   ├── checkups
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   └── views.py
│   │   ├── common
│   │   │   ├── __init__.py
│   │   │   └── models.py
│   │   ├── machines
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   └── views.py
│   │   └── profiles
│   │       ├── __init__.py
│   │       ├── models.py
│   │       └── views.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── development_sqlite.db
│   │   ├── secrets.json
│   │   └── settings.py
│   ├── manage.py
│   ├── migrations
│   │   ├── README
│   │   ├── alembic.ini
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions
│   │       ├── 4cecc0d2ed8a_.py
│   │       └── cc805ab1bc28_.py
│   └── tests
│       ├── __init__.py
│       └── test_flaskr.py
└── requirements.txt
```

> applications/* folder contains pluggable apps, which can be re used in some other projects
> applications/<app_name>/models.py contains db-model structure
> applications/<app_name>/views.py contains ClassBasedViews to handle HTTP requests
> docs/* holds all documentation related stuff
> manage.py subcommands to execute multiple tasks like, runserver, runtests, migratedb etc.
> requirements.txt contains package information
> config/ folders contains all configuration and secrets of project


Stacks : PyMongo, MongoDB, 
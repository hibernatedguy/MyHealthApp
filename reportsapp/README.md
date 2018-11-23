# MyHealthApp

ReportsApp : RESTAPIs with MongoDB support.

Fictitious health-care startup that does health checks for multiple connected instruments. The instruments currently save results via mobile client when all check-ups are done, it does the bulk upload reports.

Organziation is having a trouble with querying it's single source of truth database ( postgreSQL) and need to transforming and migrating user reports data to separate database ( NoSQL ) on periodic basis to store and serve user report data via mobile client.


# Project Structure
```
── README.md
├── config
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   └── settings.cpython-36.pyc
│   ├── secrets.json
│   └── settings.py
├── docs
│   └── ReportsAPIs.postman_collection.json
├── manage.py
├── reports
│   ├── __pycache__
│   │   ├── managers.cpython-36.pyc
│   │   ├── models.cpython-36.pyc
│   │   └── views.cpython-36.pyc
│   ├── managers.py
│   └── views.py
├── tests
└── utils
    ├── __pycache__
    │   └── response_handler.cpython-36.pyc
    └── response_handler.py
```
- config : stores all configuration stuffs
- 
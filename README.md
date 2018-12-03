# MyHealthApp

ReportsApp : RESTAPIs with MongoDB support.

Fictitious health-care startup that does health checks for multiple connected instruments. The instruments currently save results via mobile client when all check-ups are done, it does the bulk upload reports.

Organziation is having a trouble with querying it's single source of truth database ( postgreSQL) and need to transforming and migrating user reports data to separate database ( NoSQL ) on periodic basis to store and serve user report data via mobile client.

Project contains two services along with documentation,
- myhealthapp : to collect reports from doctors and machine
- reportsapp : for client's to brow the reports.

**Please go through myhealthapp/readme.md and reportsapp/readme.md file for more information**

# System Design

![alt system-design](https://github.com/codetarsier/MyHealthApp/blob/7ae896aba01040c8a575c4477f604dcdae62159d/docs/healthcheckup-system-design.jpg?raw=true)

### System Workflow
1. User comes for health checkup
2. With HealthCheckup Machine doctor does the health checkup and machine stores all these reports in it's local memory.
3. **MyHealthCheckupApp** mobile/tab application pulls those reports from HC-Machine.
4. **MyHealthCheckupApp** sends all the reports to MyHealthApp-API backend server.
5. TaskRunner runs a background task and keeps checking for the new record on some interval ( *Interval Time* can be set in settings file ). TaskRunner fetches the record and stores last **checkup-reportID** and when next time it runs, it fetches the incremental reports from previously stored checkup-reportID.
6. TaskRunner converts these reports into JSON then it sends them to **ReportsApp-Server** using ReportsAPI. 
7. Client/Customer login into ReportsApp mobile application and browse those reports from ReportsApp-API backend server.
8. When client provides username/password it gets authenticated from MyHealthApp-API.
9. After authentication user can browse Reports.

# Project Design Pattern

Highly inspired by django-design-patterns.
Following DRY principle. All applications are reusable and dependencies are kept in one folder. 

> #### Q. Why Application Folders?

Ans. **For reusability.**

```
e.g.
    profiles/
        models.py
        views.py
        managers.py     
```
If someone wants to reuse **profiles** application in some other project it's more easier to do a copy/paste instead of copying models.py, controllers.py, views.py from different folders.

> ### Q. Why ClassBasedViews instead of api's with @api decorator?

Ans. It gives more freedom in terms of creating factory methods, mixins and inheritence. Flask call it as a MethodViews.

for more details : [classbased-views method-views](http://flask.pocoo.org/docs/0.12/views/#method-views-for-apis)

> ### Q. Use of Celery and Background Job
Ans. Using threading concept to push data on different server.

# Sample Project Structure

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

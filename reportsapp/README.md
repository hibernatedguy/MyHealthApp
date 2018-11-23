# MyHealthApp

ReportsApp : RESTAPIs with MongoDB support.

Fictitious health-care startup that does health checks for multiple connected instruments. The instruments currently save results via mobile client when all check-ups are done, it does the bulk upload reports.

Organziation is having a trouble with querying it's single source of truth database ( postgreSQL) and need to transforming and migrating user reports data to separate database ( NoSQL ) on periodic basis to store and serve user report data via mobile client.

# System Design

![alt system-design](https://raw.githubusercontent.com/codetarsier/MyHealthApp/develop/docs/healthcheckup-system-design.png)

# Project Design Pattern

Highly inspired by django-design-patters.
Following DRY principle. All applications are reusable and dependencies are kept in one folder. 

> Why Application Folders?
**For reusability.**

```
e.g.
    reports/
        models.py
        views.py
        managers.py
```
If someone wants to reuse **reports** application in some other project it's more easier to do a copy/paste instead of copying models.py, controllers.py, views.py from different folders.






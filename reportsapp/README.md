# MyHealthApp

ReportsApp : RESTAPIs with MongoDB support.

Fictitious health-care startup that does health checks for multiple connected instruments. The instruments currently save results via mobile client when all check-ups are done, it does the bulk upload reports.

Organziation is having a trouble with querying it's single source of truth database ( postgreSQL) and need to transforming and migrating user reports data to separate database ( NoSQL ) on periodic basis to store and serve user report data via mobile client.

# System Design

![alt system-design](https://raw.githubusercontent.com/codetarsier/MyHealthApp/develop/docs/healthcheckup-system-design.png)

### System Workflow
1. User comes for health checkup
2. With HealthCheckup Machine doctor does the health checkup and machine stores all these reports in it's local memory.
3. MyHealthCheckupApp mobile/tab application pulls those reports from HC-Machine.
4. MyHealthCheckupApp sends all the reports to MyHealthApp-API backend server.
5. While saving all reports in postgreSQL database, post_save signal triggers and all reports goes in to a background task.
6. As soon as TaskRunner gets these reports, it sends them to ReportsApp-Server using ReportsAPI backend server. 
7. Client/Customer login into ReportsApp mobile application and browse those reports from ReportsApp-API backend server.

# Project Design Pattern

Highly inspired by django-design-patters.
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

Ans. **ClassBasedView** is a callable which takes a request and returns a response. This can be more than just a function and Flask provides it. It gives more freedom in terms of creating factory methods, mixins and inheritence. Flask call it as a MethodViews.

for more details : [classbased-views method-views](http://flask.pocoo.org/docs/0.12/views/#method-views-for-apis)

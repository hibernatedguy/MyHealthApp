# MyHealthApp

HealthApp : Yet another flask app with RESTAPIs 

Fictitious health-care startup that does health checks for multiple connected instruments. The instruments currently save results via mobile client when all check-ups are done, it does the bulk upload reports.

Organziation is having a trouble with querying it's single source of truth database ( postgreSQL) and need to transforming and migrating user reports data to separate database ( NoSQL ) on periodic basis to store and serve user report data via mobile client.


# Project Structure and Rough Model

## Accounts APP [ user information ]

> Models

```
User
    username
    password
    email
    registered_on

Profile
    user - onetoone-User
    avatar
    blood-group
    created_at

Disease
    user - onetoone-User
    name - 
    details - 
```

> APIs

```
api/v1/users/                           GET/POST/PATCH/DELETE
api/v1/<user-id>/profiles/              GET/POST/PATCH/DELETE
api/v1/users/<user-id>/disease           GET/POST/PATCH/DELETE
```



## Machine APP

> Models

```
Machine
    - machine type
    - machine information
    - manufacturor
    - created_at
```

> APIs

    api/v1/machines                         GET/POST/PATCH/DELETE

## Checkup App [ checkup information ]

> Models

```   
Checkup
    user - onetomany-User
    machine - onetomany-Machine
    checkup-type - choicefield
    checkup information
    test_taken_by
    created_at
```

> APIs

```
api/v1/checkups/      POST [ BULK UPLOAD ]
```
## Config App [ holds settings and secrets ]
```    
Secrets
    - secres.json

Environment Settings
    - development.py 
    - production.py
    - testing.py
```

# Analytics App

> APIs

``` 
user-analytics : api/v1/users/                  returns all information
user-analytics : api/v1/users/<username>/       returns checkup information for given username
```

> Sample Data Structure

```
users : [

    'user1':{
        'checkups':[
            {'checkup':'', 'created_at':''}
        ],            
    },
    'user1':{
        'checkups':[
            {'checkup':'', 'created_at':''}
        ],            
    },
    'user1':{
        'checkups':[
            {'checkup':'', 'created_at':''}
        ],            
    },
    'user1':{
        'checkups':[
            {'checkup':'', 'created_at':''}
        ],            
    },
]
```

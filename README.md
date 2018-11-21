# MyHealthApp
HealthApp : Yet another flask app with RESTAPIs 

Fictitious health-care startup that does health checks for multiple connected instruments. The instruments currently save results via mobile client when all check-ups are done, it does the bulk upload reports.

Organziation is having a trouble with querying it's single source of truth database ( postgreSQL) and need to transforming and migrating user reports data to separate database ( NoSQL ) on periodic basis to store and serve user report data via mobile client.

# Project Structure and Rough Model

- Accounts APP         [ holds all user information ]
    
    MODEL 
    --------

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

    Disese
        user - onetoone-User
        name - 
        details - 

    APIs
    --------

    api/v1/users/                           GET/POST/PATCH/DELETE
    api/v1/<user-id>/profiles/              GET/POST/PATCH/DELETE
    api/v1/users/<user-id>/Disese           GET/POST/PATCH/DELETE

- Machine APP

    Models
    --------


    Machine
        - machine type
        - machine information
        - manufacturor
        - created_at



    APIs
    --------
    api/v1/machines                         GET/POST/PATCH/DELETE


- Checkups APP       [ holds checkups done by a machine ]
    
    Checkup
        user - onetomany-User
        machine - onetomany-Machine
        checkup-type - choicefield
        checkup information
        test_taken_by
        created_at


- Configs
    
    Secrets
        - secres.json

    Environment Settings
        - development.py 
        - production.py
        - testing.py


# Project for analytics

- Analytics
    
    user-analytics : api/v1/users/                  returns all information
    user-analytics : api/v1/users/<username>/       returns checkup information for given username


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


# ReportsAPP 

ReportsApp :  Flask with MongoDB.


# Project Structure
```

├── README.md
├── config
│   ├── __init__.py
│   ├── __pycache__
│   ├── secrets.json
│   └── settings.py
├── docs
│   └── ReportsAPIs.postman_collection.json
├── manage.py
├── reports
│   ├── __pycache__
│   ├── managers.py
│   ├── models.py
│   └── views.py
├── requirements.txt
├── tests
│   ├── __init__.py
│   ├── __pycache__
│   ├── conftest.py
│   ├── flask_test.cfg
│   └── test_user_reports.py
└── utils
    ├── __pycache__
    ├── random_hex.py
    ├── response_handler.py
    └── rest_auth.py
```

- reports/* directoru contains apis and report manager
- reports/manager.py is mongodb wrapper to interact with mongodb for CRUD operations
- reports/views is api like classbased views
- utils/rest-auth **authenticate username/password by calling myhealthapp's login api**
- utils/responsehandler for custom responses


# Models
```
User
    username
    
Reports
    username
    report_details  
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

# APIs
[Postman Api Doc](https://documenter.getpostman.com/view/227044/RzfZQD9a)

# Tests
- Postman E2E test is available with postmanin collection in **docs/** directory
- PyTest is available in **tests/** directory
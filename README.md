# User Microservice [![Build Status](https://travis-ci.org/dechristo/user-microservice.svg?branch=master)](https://travis-ci.org/dechristo/user-microservice)

Developed in Python3 (with Flask) and MySQL.

## 1. Setup
## 1.1 Installing virtual envrironment
Type `virtualenv -p python3 env`

### 1.2 Install dependencies
Activate the virtual environment and type:

 `pip install -r requirements.txt`

### 1.3 Setting environment variable
Add `FLASK_APP=router.py` to the environemtn vars.

### 1.4 Starting the virtual environment
Type `source env/bin/activate` if you are on linux/osx.

In case you are using windows:

`/env/Scripts/activate.bat`

### 1.5 Starting

At the root project folder type `python -m flask run`

You should see the output:

         * Serving Flask app "router.py"       
         * Debug mode: off
         * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

## 2. Unit Tests
Simply type `pytest` at the project's root folder.
         
## 3. Endpoints

### 3.1 Microservice status
Request: 

`GET /api/status-check`

Response:

    {
	    "msg": "user microservice running..."
	}

### 3.2 Add user
Request: 

`POST /api/user`

 Body:
 
    {
        "username": "Luke",
        "first_name": "Luke",
        "last_name": "Skywalker",
        "password": "theforce",
        "access_level": 99,
        "email": "lskywalker@sw.com"
    }

Response:

    {
	    "info": "user successfully created."
    }
       
       
### 3.3 Delete user
Request: 

`DELETE /api/user/:id`
    
Response:

    {
	    "info": "user successfully deleted."
    } 
    
 or if user does not exists:
    
    {
	    "error": "user could not be deleted because it wasn't found."
    }
    
### 3.4 Get one user
Request: 

`GET /api/user/:id`
    
Response:

    {
        "access_level": 99,
        "email": "lskywalker@sw.com",
        "first_name": "Luke",
        "id": 10,
        "last_name": "Skywalker",
        "username": "Luke"
    }
    

Returns `404` if user not found.

### 3.5 Get all users

Request: 

`GET /api/users`
    
Response:

    {
        "data": [
            {
                "id": 17,
                "access_level": 99,
                "email": "lskywalker@sw.com",
                "first_name": "Luke",			
                "last_name": "Skywalker",
                "username": "Luke"
            },
            {
                "id": 18,
                "access_level": 5,
                "email": "jaden@sw.com",
                "first_name": "Jaden",			
                "last_name": "Skywalker",
                "username": "jaden"
            },
            {
                "id": 24,
                "access_level": 0,
                "email": "mitcho.betao@gmail.com",
                "first_name": "Chatuba",			
                "last_name": "de Mesquita",
                "username": "chapiscoloco"
            }
        ]
    }
    

Returns `404` if user not found.

### 3.6 Update user
Request: 

`PUT /api/user/<id>`
    
  Body:
  
    {
        "username": "Luke",
        "first_name": "Luke",
        "last_name": "Skywalker",
        "password": "theforce",
        "access_level": 99,
        "email": "lskywalker@sw.com"
    }
    
Response:

    {
        "info": "User information successfully updated."
    }
    
   or if an error occurred during update:
    
    {
	    "error": "Could not update user information."
    }
### 3.7 Search user
Request: 

`GET /api/user?name={name}`
    
    
 Query parameters:
    
    - name: user's first and/or last name
    
e.g.:

`GET /api/user?name=Luke%20Skywalker`

Response:

    {
        "access_level": 99,
        "email": "lskywalker@sw.com",
        "first_name": "Luke",
        "id": 10,
        "last_name": "Skywalker",
        "username": "Luke"
    }
    

Returns `404` if user not found.
## TechQuiz API

It is a technical quiz API, build purely using Python (programming language), Django and Django-Rest-Framework (opensource framework written in python).

### Current Features
Listing the features of the API
- Custom User Model (with email and username as unique mandatory fields)
- Profile Model (auto-created when user register using signals)
- One-To-One Relationship b/w Custom-User and Profile Model
- JWT (Json-Web-Token) Authentication 

### API EndPoints

API Endpoints defines the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE.

| Endpoint | HTTP Method | CURD Method | Result |
|---|---|---|---|
| ```user/register``` | POST | CREATE | Create a new user |
| ```token```  | POST | CREATE | Create auth token |
| ```search/:username```  | GET  | READ  | Get a user profile |

- <b>User Registration</b> (Creating a New User)
    - <b>POST</b> 
    ```http://localhost:8000/api/user/register/```
    ```
    {
        "email": "testuser2@gmail.com",
        "user_name": "testuser2",
        "password": "testuser2"
    }
    ```

- <b>Access Token/Refresh Token</b>
    - <b>POST</b> 
    ```http://localhost:8000/api/token/```
    ```
    {
        "email": "testuser2@gmail.com",
        "password": "testuser2"
    }   
    ```

- <b>Search Profiles</b>
    - <b>GET</b>
    ```http://localhost:8000/api/search/testuser2```
    ```
    {
        "id": 3,
        "user": {
            "user_name": "testuser2",
            "email": "testuser2@gmail.com"
        },
        "about": "Hello, I am testuser2.",
        "location": "India",
        "birth_date": "2021-01-01",
        "gender": "Male"
    }
    ```
### Upcoming Features
Listing the upcoming features of the API
- Profile Model API Endpoints (Update Profile)
- Create Tech Quiz Model
- Tech Quiz Model API Endpoints

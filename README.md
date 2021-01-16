## TechQuiz API

It is a technical quiz API, build purely using Python (programming language), Django and Django-Rest-Framework (opensource framework written in python).

### Current Features
Listing the features of the API
- Custom User Model (with email and username as unique mandatory fields)
- Profile Model (auto-created when user register using signals)
- One-To-One Relationship b/w Custom-User and Profile Model
- JWT (Json-Web-Token) Authentication 

### API EndPoints

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

### Upcoming Features
Listing the upcoming features of the API
- Profile Model API Endpoints
- Create Tech Quiz Model
- Tech Quiz Model API Endpoints

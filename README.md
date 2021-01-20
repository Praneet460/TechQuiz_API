## TechQuiz API

It is a technical quiz API, build purely using Python (programming language), Django and Django-Rest-Framework (opensource framework written in python).

### Current Features
Listing the features of the API
- Custom User Model (with email and username as unique mandatory fields)
- Profile Model (auto-created when user register using signals)
- One-To-One Relationship b/w Custom-User and Profile Model
- JWT (Json-Web-Token) Authentication 
- Authenticated users can only update their own User Profile

### API EndPoints

API Endpoints defines the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE.

| Endpoint | HTTP Method | CURD Method | Result |
|---|---|---|---|
| ```user``` | POST | CREATE | Create a new user |
| ```search/<user_name>``` | GET  | READ  | Get a user profile |
| ```token``` | POST | CREATE | Create access & refresh token |
| ```token/refresh``` | POST | CREATE | Get new access token |
| ```profile/<user_name>``` | GET, PUT, PATCH | READ & UPDATE | Get a user profile and update your profile |

- <b>User Registration</b> (Creating a New User)
    - <b>POST</b> 
    ```http://localhost:8000/api/v1/user/```
        - <b>Body</b>
            ```
            {
                "email": "testuser2@gmail.com",
                "user_name": "testuser2",
                "password": "testuser2"
            }
            ```

- <b>Search Profiles</b>
    - <b>GET</b>
    ```http://localhost:8000/api/v1/search/testuser2```
        - <b>Response</b>
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

- <b>Access Token/Refresh Token</b>
    - <b>POST</b> 
    ```http://localhost:8000/api/v1/token/```
        - <b>Body</b>
            ```
            {
                "email": "testuser2@gmail.com",
                "password": "testuser2"
            }   
            ```

- <b>Refresh Token</b>
    - <b>POST</b>
    ```http://localhost:8000/api/v1/token/refresh/```
        - <b>Body</b>
            ```
            {
                "email": "testuser2@gmail.com",
                "password": "testuser2",
                "refresh": <your-refresh-token>
            }
            ```

- <b>User Profile</b> (Required Access Token for Authentication)
    - <b>GET</b>
    ```http://localhost:8000/api/v1/profile/testuser1```
        - <b>Response</b>
            ```
            {
                "id": 5,
                "about": "Hello, I am modified testuser1.",
                "location": "India",
                "birth_date": "2020-01-11",
                "gender": "Male"
            }
            ```
    - <b>PUT</b>
    ```http://localhost:8000/api/v1/profile/testuser1/```
        - <b>Body</b>
            ```
            {
                "about": "Hello, I am testuser1.",
                "location": "Australia",
                "birth_date": "2020-01-11",
                "gender": "Male"
            }
            ```
    - <b>PATCH</b>
    ```http://localhost:8000/api/v1/profile/testuser1/```
        - <b>Body</b>
            ```
            {  
                "location": "India",
                "birth_date": "2020-01-21"
            }
            ```



### Upcoming Features
Listing the upcoming features of the API
- Create Tech Quiz Model
- Tech Quiz Model API Endpoints
- User can delete own account
- User can create Tech Quiz
- View TestCase
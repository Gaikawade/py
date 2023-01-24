# Flask and MySQL Login Page
A simple Flask Login Application with MySQL database
* Flask_mysqldb package is used to connect to MySQL database

#### 1. Requirements
* Python 3.x
* Flask

#### 2. Create a virtural environment
```pip -m venv <env_name>```

#### 3. Activate the virtual environment 
```.\venv\Scripts\activate (For Windows)```

#### 4. For installing dependencies
```pip install -r requirements.txt```


#### 5. Run the application
```python app.py```

#### POST/register

* Using form data we get the Name, Email and Password
* Create a new column with the given input in our database
* Once registrtion is done we will show a message and redirect them to the login page 

#### POST/login

* Using form data as the content type
* User need to login using their own email and password
* Check for that particular email and password in the DBI
  1. If found then redirect them to the home page, store the user details in a session
  2. If not send them a appropriate message


#### /logout

* In the home page logout functionality will be provided
* Once the logged in user click on logout, we remove the session data which is stored at the time of log-in and redirect them to the login page
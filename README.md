# Neighbourhood
Neighbourhood web application that allows members of the same hood to interact through posting, can view the emergency details and businesses in that hood.

## Prerequisites
- Have Git installed.
- Have Python and Pip Installed
- Have a text editor or an IDE installed e.g VS Code, Atom
### Technologies Used
- Python, Django, JavaScript, CSS and HTML
- VS Code.
### Setup Installation
To run the application:-
1. Clone the repository to a folder in your machine using `https://github.com/ABERT-NOLA/neighbourhood.git`
2. Cd to that folder.
3. Create a virtual environment using `python3 -m venv virtual`
4. Activate the virtual environment using `source virtual/bin/activate`
##### Add the following to the env file
  ```bash
 SECRET_KEY = your secret key
 DEBUG=TRUE
 DB_NAME=''
 DB_USER='database user name'
 DB_PASSWORD='database password'
 DB_HOST='127.0.0.1'
 MODE='dev'
 ALLOWED_HOSTS='*'
 DISABLE_COLLECTSTATIC=1
 EMAIL_USE_TLS = True
 EMAIL_HOST = 'smtp.gmail.com'
 EMAIL_PORT = 587
 EMAIL_HOST_USER = 'your email'
 EMAIL_HOST_PASSWORD = '<>'
 ```
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
 python manage.py makemigrations gallery
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
```  

#### Author
- Albert Obwoge 
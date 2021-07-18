# Think About
## Tiny articles worth thinking about

# Steps for run project
## Clone repository
Enter your git **Username** and git **Password**
```shell
$ git clone https://github.com/TilekTekinov/think_about.git
```
Go to project directory
```shell
$ cd think_about/
```

### Create virtual environment
```shell
$ python3 -m venv my-project-env
```
If you don't have `python3-venv` package <br>
Install on Linux
```shell
$ sudo apt install python3-venv
```
When virtual environment created activate it
```shell
$ source env/bin/activate
```
Install all requirements from requirements.txt
```shell
$ pip install -r requirements.txt
```

### Create database
Project use `postgres` database, you need install on your system <br>
If `postgres` installed, create **db** and **db_user**
```shell
$ sudo su postgres
$ psql template1
template1=# CREATE USER "user_name" WITH PASSWORD 'user_password';
template1=# CREATE DATABASE "database_name" OWNER "user_name";
template1=# GRANT ALL PRIVILEGES ON DATABASE "database_name" to user_name;
template1=# \q
$ exit
```

### Environment variables
Create .env file in project root
```shell
$ touch .env
```
And use this .env example
```dotenv
SECRET_KEY = your_sercret_key

DB_NAME = db_name 
DB_USER = db_user
DB_PASSWORD = db_password
DB_HOST = db_host
DB_PORT = db_port
```
You can generate **secret_key** from
```shell
$ python manage.py secret_key
```
Or use this command directly
```shell
$ python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Preparations
Make migrations
```shell
$ python manage.py makemigrations
```
Make migrate for create tables
```shell
$ python manage.py migrate
```
Make collect static
```shell
$ python manage.py collectstatic
```

### Create super user
```shell
$ python manage.py createsuperuser
```

### Run project
Finally, you can run the project and test
```shell
$ python manage.py runserver
```

### Documentations
For generate documentations use follow command in `docs` folder
```shell
/docs$ make html
```
It's generate all project documentations

Open in browser `index.html`
```
<project_dir>/docs/_build/html/index.html
```
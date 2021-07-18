Quick Start Guide
=================


Download Think_About Django Project Boilerplate
-----------------------------------------------

First, you need to download the BoilerPlate from GitHub.


Create virtual environment
--------------------------

Create a Development virtual environment with Python 3 installed::

    $ python3 -m venv my-project-env

When virtual environment created activate it::

    $ source env/bin/activate

Install all requirements from requirements.txt::

    $ pip install -r requirements.txt


Create database
---------------

Project use **postgres** database, you need install on your system

If **postgres** installed, create **db** and **db_user**::

    $ sudo su postgres
    $ psql template1
    template1=# CREATE USER "user_name" WITH PASSWORD 'user_password';
    template1=# CREATE DATABASE "database_name" OWNER "user_name";
    template1=# GRANT ALL PRIVILEGES ON DATABASE "database_name" to user_name;
    template1=# \q
    $ exit


Environment variables
---------------------

Create .env file in project root::

    $ touch .env

And use this .env example::

    SECRET_KEY = your_sercret_key

    DB_NAME = db_name
    DB_USER = db_user
    DB_PASSWORD = db_password
    DB_HOST = db_host
    DB_PORT = db_port


Secret Django Key
-----------------

This boilerplate has the **DJANGO_KEY** setting variable hidden.

You can generate your DJANGO_KEY |django_key|.

.. |django_key| raw:: html

    <a href="http://www.miniwebtool.com/django-secret-key-generator"
    target="_blank">here</a>

Or use including generator secret_key::

    $ python manage.py secret_key

Or use this command directly::

    $ python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"


Preparations
------------


Make migrations::

    $ python manage.py makemigrations

Make migrate for create tables::

    $ python manage.py migrate

Make collect static::

    $ python manage.py collectstatic


Create super user
-----------------
::

    $ python manage.py createsuperuser

Run project
-----------


Finally, you can run the project and test::

    $ python manage.py runserver

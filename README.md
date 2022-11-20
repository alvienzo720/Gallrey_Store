# Art Gallery App

This is a project  built using Python Django Framework to enable users upload photos, and reset password.

## Warnings

Please be sure to read the following instructions and considerations before running this code on your local workstation, shared systems, or production environments.


## Local development

To run this project in your development machine, follow these steps:

1. (optional) Create and activate a [virtualenv](https://virtualenv.pypa.io/) (you may want to use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/)).


2. Fork this repo and clone your fork:

    `git clone https://github.com/alvienzo720/Gallrey_Store`

3. Install dependencies:

    `pip install -r requirements.txt`

3. Make migrations to database:

    `./manage.py makemigrate`

4. Create a development database:

    `./manage.py migrate`

4. Create a superuser database:

    `./manage.py createsuperuser`



5. If everything is alright, you should be able to start the Django development server:

    `./manage.py runserver`

6. Open your browser and go to http://127.0.0.1:8000, you will be greeted with a welcome page.


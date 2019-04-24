# Developer Guide

## Getting Started

### Prerequisites
- [python3.6](https://www.python.org/downloads/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [postgresql](https://www.postgresql.org/docs/10/release-10-6.html)

### Initialize the project

Create and activate a virtualenv:
(Make sure to activate virtual environment with python version 3.6)

```bash
virtualenv --python=python3 venv
source venv/bin/activate
```
If your python3 points to python3.5 or lower, use ```python3.6``` to create the virtual environment.

Install dependencies:

```bash
pip install -r requirements.txt
```

Database setup - Login to postgres and create db with name ```instawork```:
```bash
create database instawork;
```

Migrate, and run the server:
```bash
python manage.py migrate
python manage.py runserver
```
This project has fixtures. If you want to load some default data use these commands in the same order:
```bash
python manage.py loaddata initial_data
```

### Running test Cases
Use the following command to run test cases in all apps.

```bash
python manage.py test
```

### API Documentation
Use swagger for api(GET, POST, PUT, PATCH, DELETE) doumentaion. Try below url in your browser after running your server - 

```bash
http://localhost:8000/swagger/
```

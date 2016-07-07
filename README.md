# App 1.0

## Dependencies:

- sudo apt-get update

- sudo apt-get install binutils libproj-dev postgresql-9.3 postgresql-9.3-postgis-2.1 postgresql-server-dev-9.3 python-psycopg2

- sudo apt-get install python-pip (if needed)

## CD into the project directory
- git clone git@github.com:stellasstar/flask_app.git

- cd flask_app

## Set up the virtual environment
- virtualenv --setuptools venv 
- source venv/bin/activate
- cd flask_app

## Install other dependencies through pip 
- pip install -r requirements.txt --upgrade -e .

## Configuring PostgreSQL:

Ensure that there is a line in /etc/postgresql/9.3/main/pg_hba.conf that allows local connections using md5:
- edit /etc/postgresql/9.3/main/pg_hba.conf to look like the line below

- "local" is for Unix domain socket connections only local all all md5

## Install database
- ./builddb.sh 

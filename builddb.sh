#!/bin/bash

NAME=preregistation
USER=preregistration
PASSWORD=password

sudo -u postgres psql -c "DROP DATABASE $NAME" 
sudo -u postgres psql -c "DROP USER $USER" 
sudo -u postgres psql -c "CREATE ROLE $USER PASSWORD 'password'" 
sudo -u postgres psql -c "CREATE DATABASE $NAME WITH OWNER = $USER"

sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $NAME to $USER"; 

#!/bin/bash
echo "Waiting for database."
sleep 10s
python manage.py migrate 
echo "Starting server"
python -u manage.py runserver 0.0.0.0:8888
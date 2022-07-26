@echo off
title runsever
start cmd /k " cd F:\blog\venv\Scripts && activate && cd ../.. && python manage.py runserver"
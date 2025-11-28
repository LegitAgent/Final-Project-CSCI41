@echo off
(FOR /d /r . %%d IN (migrations) DO @IF EXIST "%%d" rd /s /q "%%d")  &&^
psql -U finaluser -c "DROP DATABASE IF EXISTS finalproject;" -c "CREATE DATABASE finalproject;" &&^
cd ../env/scripts && activate && cd ../../FinalProjectCSCI41 &&^
python manage.py makemigrations account central_bookings &&^
python manage.py migrate && python manage.py createsuperuser --no-input && deactivate && pause
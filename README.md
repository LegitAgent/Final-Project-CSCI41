# Final-Project-CSCI41
This project was created for our CSCI 41 (Information Management) final requirement.
Edit the .env.example file as needed to be a .env file with corresponding text inputs.

Follow the instructions below if you already have python, postgres, and git installed.

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/Final-Project-CSCI41.git
cd Final-Project-CSCI41
```

## 2. Make a Python Virtual Environment
```bash
python -m venv env
env\Scripts\activate
```

## 3. Install requirements.txt
```bash
pip install -r requirements.txt
```

## 4. Setup Environment Variables
Copy and edit the .env.example file to store all senestive information suchn as passwords, database credentials and etc.
Make sure to edit the file name to `.env`.

## 5. Set Up PostgreSQL
Assuming you have PostgreSQL installed, the command below should prompt you for your postgreSQL password.
```bash
psql -U postgres
```
Then create the user:
```sql
CREATE USER finaluser WITH PASSWORD 'yourpassword';
```

## 6. Run Initial Migrations
**For Windows ONLY**<br>
A setup batch file has been provided to automate database creation from scratch. It also creates
a python superuser for the admin site. Simply click on `setup.bat` to run.

**Otherwise, proceed manually**
```bash
python manage.py migrate
```

## 7. Run the Server
**For Windows ONLY**<br>
A setup batch file has been provided to automate running the server. Simply click on `run.bat` to run.

**Otherwise, proceed manually**
```bash
python manage.py runserver
```
The project should now be running at http://127.0.0.1:8000/

## SUPER IMPORTANT NOTES
- All environment-specific settings are stored in .env.
- Make sure you never commit .env or your actual database credentials.
- Use .env.example as a template for others.


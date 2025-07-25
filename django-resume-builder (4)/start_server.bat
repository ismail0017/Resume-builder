@echo off
echo Starting Django Resume Builder...

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Start the development server
python manage.py runserver

pause

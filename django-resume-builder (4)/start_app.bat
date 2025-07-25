@echo off
echo Starting Django Resume Builder...

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install missing packages if needed
pip install django-environ==0.11.2 --quiet

REM Run the complete setup
python complete_setup.py

REM Start the development server
echo.
echo Starting development server...
python manage.py runserver

pause

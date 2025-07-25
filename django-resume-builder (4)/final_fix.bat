@echo off
echo Fixing Django Resume Builder - Final Solution

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run the fix script
python fix_user_model.py

REM Install essential packages
pip install django-environ==0.11.2 Django==4.2.7 django-allauth==0.57.0 Pillow==10.0.1 reportlab==4.0.4 python-docx==1.1.0

REM Setup database with fixed models
echo Setting up database...
python manage.py makemigrations
python manage.py migrate

REM Create superuser
echo.
echo Creating superuser...
python manage.py createsuperuser

echo.
echo ========================================
echo Django Resume Builder is ready!
echo Starting server...
echo ========================================

REM Start server
python manage.py runserver

pause

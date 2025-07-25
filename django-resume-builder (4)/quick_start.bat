@echo off
echo Quick Start - Django Resume Builder

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install essential packages
pip install django-environ==0.11.2 Django==4.2.7 django-allauth==0.57.0 Pillow==10.0.1 --quiet

REM Create .env file if it doesn't exist
if not exist .env (
    echo DEBUG=True > .env
    echo SECRET_KEY=django-insecure-dev-key-change-in-production-12345 >> .env
    echo ALLOWED_HOSTS=localhost,127.0.0.1,* >> .env
    echo EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend >> .env
)

REM Setup database
python manage.py makemigrations
python manage.py migrate

echo.
echo ========================================
echo Django Resume Builder is ready!
echo Starting server...
echo ========================================

REM Start server
python manage.py runserver

pause

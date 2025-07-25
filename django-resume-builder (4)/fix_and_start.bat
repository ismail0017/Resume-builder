@echo off
echo Fixing Django Resume Builder Installation...

REM Make sure we're in the virtual environment
call venv\Scripts\activate.bat

REM Install missing packages
echo Installing missing packages...
pip install djangorestframework-simplejwt==5.3.0
pip install djoser==2.2.0
pip install drf-spectacular==0.26.5

REM Create a backup of current settings
if exist core\settings.py (
    copy core\settings.py core\settings_backup.py
    echo Backed up original settings
)

REM Use simplified settings temporarily
copy core\settings_simple.py core\settings.py
copy core\urls_simple.py core\urls.py
copy resume_builder\models_simple.py resume_builder\models.py

echo Running database setup...
python manage.py makemigrations
python manage.py migrate

echo Creating superuser...
python manage.py createsuperuser --email admin@example.com --noinput || echo "Superuser creation skipped"

echo.
echo ========================================
echo Setup completed successfully!
echo.
echo To start the server:
echo python manage.py runserver
echo.
echo Then visit: http://127.0.0.1:8000
echo ========================================
pause

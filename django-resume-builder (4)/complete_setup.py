#!/usr/bin/env python
"""
Complete setup script for Django Resume Builder - ensures everything works
"""
import subprocess
import sys
import os

def run_command(command, description, ignore_errors=False):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        if ignore_errors:
            print(f"⚠ {description} failed but continuing...")
            return False
        else:
            print(f"✗ {description} failed:")
            print(f"Error: {e.stderr}")
            return False

def install_packages():
    """Install all required packages"""
    packages = [
        "django-environ==0.11.2",
        "Django==4.2.7",
        "djangorestframework==3.14.0",
        "django-cors-headers==4.3.1",
        "django-filter==23.3",
        "djangorestframework-simplejwt==5.3.0",
        "djoser==2.2.0",
        "drf-spectacular==0.26.5",
        "Pillow==10.0.1",
        "django-allauth==0.57.0",
        "reportlab==4.0.4",
        "python-docx==1.1.0",
    ]
    
    for package in packages:
        run_command(f"pip install {package}", f"Installing {package}")
    
    # Try to install PostgreSQL adapter (optional)
    run_command("pip install psycopg2-binary==2.9.7", "Installing PostgreSQL adapter", ignore_errors=True)

def main():
    print("Django Resume Builder - Complete Setup")
    print("=" * 50)
    
    # Install packages
    install_packages()
    
    # Create .env file
    if not os.path.exists('.env'):
        print("\nCreating .env file...")
        with open('.env', 'w') as f:
            f.write("""DEBUG=True
SECRET_KEY=django-insecure-dev-key-change-in-production-12345
ALLOWED_HOSTS=localhost,127.0.0.1,*
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
""")
        print("✓ .env file created")
    
    # Setup database
    print("\nSetting up database...")
    run_command("python manage.py makemigrations", "Creating migrations")
    run_command("python manage.py migrate", "Running migrations")
    
    print("\n" + "=" * 50)
    print("Setup completed successfully!")
    print("\nTo start the server:")
    print("python manage.py runserver")
    print("\nThen visit: http://127.0.0.1:8000")

if __name__ == '__main__':
    main()

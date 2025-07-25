#!/usr/bin/env python
"""
Quick setup script for Resume Builder - handles common setup issues
"""
import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def main():
    print("Django Resume Builder - Quick Setup")
    print("=" * 40)
    
    # Check if we're in a virtual environment
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✓ Virtual environment detected")
    else:
        print("⚠ Warning: No virtual environment detected")
        print("It's recommended to use a virtual environment")
        response = input("Continue anyway? (y/N): ")
        if response.lower() != 'y':
            print("Setup cancelled. Please create a virtual environment first:")
            print("python -m venv venv")
            print("venv\\Scripts\\activate  # Windows")
            print("source venv/bin/activate  # Linux/Mac")
            return
    
    # Update pip
    run_command("python -m pip install --upgrade pip", "Updating pip")
    
    # Install core dependencies first
    core_packages = [
        "Django==4.2.7",
        "django-environ==0.11.2",
        "Pillow==10.0.1",
    ]
    
    for package in core_packages:
        run_command(f"pip install {package}", f"Installing {package}")
    
    # Install other dependencies
    other_packages = [
        "djangorestframework==3.14.0",
        "django-cors-headers==4.3.1",
        "django-filter==23.3",
        "django-allauth==0.57.0",
        "reportlab==4.0.4",
        "python-docx==1.1.0",
    ]
    
    for package in other_packages:
        run_command(f"pip install {package}", f"Installing {package}")
    
    # Try to install psycopg2-binary (might fail on some systems)
    print("\nTrying to install PostgreSQL adapter...")
    if not run_command("pip install psycopg2-binary==2.9.7", "Installing PostgreSQL adapter"):
        print("PostgreSQL adapter installation failed. Using SQLite instead.")
        print("You can still use the application with SQLite database.")
    
    # Create .env file if it doesn't exist
    if not os.path.exists('.env'):
        print("\nCreating .env file...")
        with open('.env', 'w') as f:
            f.write("""# Django Resume Builder Environment Variables
DEBUG=True
SECRET_KEY=django-insecure-dev-key-change-in-production-12345
ALLOWED_HOSTS=localhost,127.0.0.1,*

# Database (SQLite by default)
# DB_ENGINE=django.db.backends.sqlite3
# DB_NAME=db.sqlite3

# Email (Console backend for development)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
""")
        print("✓ .env file created")
    
    # Run migrations
    print("\nSetting up database...")
    if run_command("python manage.py makemigrations", "Creating migrations"):
        run_command("python manage.py migrate", "Running migrations")
    
    # Create superuser
    print("\nCreating superuser...")
    print("You'll be prompted to create an admin user.")
    try:
        subprocess.run("python manage.py createsuperuser", shell=True, check=True)
        print("✓ Superuser created successfully")
    except subprocess.CalledProcessError:
        print("Superuser creation skipped or failed")
    
    print("\n" + "=" * 40)
    print("Setup completed!")
    print("\nTo start the development server:")
    print("python manage.py runserver")
    print("\nThen visit: http://127.0.0.1:8000")
    print("\nAdmin panel: http://127.0.0.1:8000/admin")

if __name__ == '__main__':
    main()

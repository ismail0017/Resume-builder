#!/usr/bin/env python
"""
Database creation and migration script for Resume Builder
"""
import os
import sys
import django
from django.core.management import execute_from_command_line

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Setup Django
django.setup()

def create_database():
    """Create database tables and run migrations"""
    print("Creating database tables...")
    
    # Make migrations
    execute_from_command_line(['manage.py', 'makemigrations'])
    
    # Run migrations
    execute_from_command_line(['manage.py', 'migrate'])
    
    print("Database tables created successfully!")

def create_superuser():
    """Create a superuser for admin access"""
    from django.contrib.auth import get_user_model
    
    User = get_user_model()
    
    if not User.objects.filter(email='admin@resumebuilder.com').exists():
        User.objects.create_superuser(
            email='admin@resumebuilder.com',
            password='admin123',
            first_name='Admin',
            last_name='User'
        )
        print("Superuser created: admin@resumebuilder.com / admin123")
    else:
        print("Superuser already exists")

if __name__ == '__main__':
    create_database()
    create_superuser()
    print("Setup completed successfully!")

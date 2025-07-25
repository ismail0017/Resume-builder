import os
import sys
import subprocess
import django
from django.core.management import execute_from_command_line

def setup_django():
    """Setup Django environment and run the application"""
    
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    
    # Setup Django
    django.setup()
    
    print("Setting up Django Resume Builder...")
    
    # Create migrations
    print("Creating migrations...")
    execute_from_command_line(['manage.py', 'makemigrations'])
    
    # Run migrations
    print("Running migrations...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Create superuser programmatically
    print("Creating superuser...")
    from django.contrib.auth.models import User
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@resumebuilder.com',
            password='admin123'
        )
        print("Superuser created: admin / admin123")
    
    # Create sample data
    create_sample_data()
    
    print("Setup completed successfully!")
    print("Starting development server...")
    
    # Start the development server
    execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:8000'])

def create_sample_data():
    """Create sample resume data"""
    from django.contrib.auth.models import User
    from resume_builder.models import PersonalInfo, WorkExperience, Education, Project, TechnicalSkill, Resume
    from datetime import date
    
    # Get or create a sample user
    user, created = User.objects.get_or_create(
        username='john_doe',
        defaults={
            'email': 'john.doe@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }
    )
    
    if created:
        user.set_password('password123')
        user.save()
    
    # Create personal info
    personal_info, created = PersonalInfo.objects.get_or_create(
        user=user,
        defaults={
            'full_name': 'John Doe',
            'email': 'john.doe@example.com',
            'phone': '+1 (555) 123-4567',
            'address': '123 Main St, San Francisco, CA 94105',
            'linkedin': 'https://linkedin.com/in/johndoe',
            'github': 'https://github.com/johndoe',
            'website': 'https://johndoe.dev',
            'summary': 'Experienced Full Stack Developer with 5+ years of experience in building scalable web applications using modern technologies.'
        }
    )
    
    # Create work experience
    WorkExperience.objects.get_or_create(
        user=user,
        company='Tech Solutions Inc.',
        position='Senior Full Stack Developer',
        defaults={
            'location': 'San Francisco, CA',
            'start_date': date(2022, 1, 1),
            'current': True,
            'description': 'Lead development of microservices architecture serving 1M+ users. Built RESTful APIs using Django and React frontend.'
        }
    )
    
    # Create education
    Education.objects.get_or_create(
        user=user,
        institution='University of California, Berkeley',
        degree='Bachelor of Science',
        defaults={
            'field_of_study': 'Computer Science',
            'location': 'Berkeley, CA',
            'start_date': date(2016, 8, 1),
            'end_date': date(2020, 5, 1),
            'gpa': 3.8
        }
    )
    
    # Create project
    Project.objects.get_or_create(
        user=user,
        title='E-commerce Platform',
        defaults={
            'description': 'Built a full-featured e-commerce platform with user authentication, payment processing, and admin dashboard.',
            'technologies': 'Django, React, PostgreSQL, Redis, Stripe API',
            'start_date': date(2023, 1, 1),
            'end_date': date(2023, 6, 1),
            'github_url': 'https://github.com/johndoe/ecommerce-platform'
        }
    )
    
    # Create technical skills
    skills = [
        {'name': 'Python', 'category': 'programming', 'proficiency': 5},
        {'name': 'JavaScript', 'category': 'programming', 'proficiency': 5},
        {'name': 'Django', 'category': 'framework', 'proficiency': 5},
        {'name': 'React', 'category': 'framework', 'proficiency': 4},
    ]
    
    for skill_data in skills:
        TechnicalSkill.objects.get_or_create(
            user=user,
            name=skill_data['name'],
            defaults=skill_data
        )
    
    # Create sample resume
    Resume.objects.get_or_create(
        user=user,
        title='Software Developer Resume',
        defaults={'template': 'modern'}
    )
    
    print(f"Sample data created for user: {user.username}")

if __name__ == '__main__':
    setup_django()

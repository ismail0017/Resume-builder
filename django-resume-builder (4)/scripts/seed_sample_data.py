#!/usr/bin/env python
"""
Seed sample data for Resume Builder
"""
import os
import sys
import django
from datetime import date, timedelta

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Setup Django
django.setup()

from django.contrib.auth import get_user_model
from resume_builder.models import (
    PersonalInfo, WorkExperience, Education, Project, 
    Certification, Award, Language, TechnicalSkill, Resume
)

User = get_user_model()

def create_sample_user():
    """Create a sample user with complete resume data"""
    
    # Create user
    user, created = User.objects.get_or_create(
        email='john.doe@example.com',
        defaults={
            'first_name': 'John',
            'last_name': 'Doe',
            'password': 'pbkdf2_sha256$600000$test$test'  # password: testpass123
        }
    )
    
    if created:
        user.set_password('testpass123')
        user.save()
        print(f"Created user: {user.email}")
    
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
            'summary': 'Experienced Full Stack Developer with 5+ years of experience in building scalable web applications using modern technologies. Passionate about clean code, user experience, and continuous learning.'
        }
    )
    
    # Create work experiences
    work_experiences = [
        {
            'company': 'Tech Solutions Inc.',
            'position': 'Senior Full Stack Developer',
            'location': 'San Francisco, CA',
            'start_date': date(2022, 1, 1),
            'end_date': None,
            'current': True,
            'description': 'Lead development of microservices architecture serving 1M+ users. Built RESTful APIs using Django and React frontend. Mentored junior developers and improved code quality through code reviews.'
        },
        {
            'company': 'StartupXYZ',
            'position': 'Full Stack Developer',
            'location': 'San Francisco, CA',
            'start_date': date(2020, 6, 1),
            'end_date': date(2021, 12, 31),
            'current': False,
            'description': 'Developed and maintained web applications using Python, Django, and JavaScript. Collaborated with cross-functional teams to deliver features on time. Implemented automated testing and CI/CD pipelines.'
        }
    ]
    
    for exp_data in work_experiences:
        WorkExperience.objects.get_or_create(
            user=user,
            company=exp_data['company'],
            position=exp_data['position'],
            defaults=exp_data
        )
    
    # Create education
    education_data = {
        'institution': 'University of California, Berkeley',
        'degree': 'Bachelor of Science',
        'field_of_study': 'Computer Science',
        'location': 'Berkeley, CA',
        'start_date': date(2016, 8, 1),
        'end_date': date(2020, 5, 1),
        'current': False,
        'gpa': 3.8,
        'description': 'Relevant coursework: Data Structures, Algorithms, Database Systems, Software Engineering'
    }
    
    Education.objects.get_or_create(
        user=user,
        institution=education_data['institution'],
        degree=education_data['degree'],
        defaults=education_data
    )
    
    # Create projects
    projects = [
        {
            'title': 'E-commerce Platform',
            'description': 'Built a full-featured e-commerce platform with user authentication, payment processing, and admin dashboard. Implemented real-time inventory management and order tracking.',
            'technologies': 'Django, React, PostgreSQL, Redis, Stripe API',
            'start_date': date(2023, 1, 1),
            'end_date': date(2023, 6, 1),
            'current': False,
            'github_url': 'https://github.com/johndoe/ecommerce-platform',
            'live_url': 'https://ecommerce-demo.johndoe.dev'
        },
        {
            'title': 'Task Management App',
            'description': 'Developed a collaborative task management application with real-time updates, file attachments, and team collaboration features.',
            'technologies': 'Django, Vue.js, WebSockets, PostgreSQL',
            'start_date': date(2022, 8, 1),
            'end_date': date(2022, 12, 1),
            'current': False,
            'github_url': 'https://github.com/johndoe/task-manager',
            'live_url': 'https://tasks.johndoe.dev'
        }
    ]
    
    for project_data in projects:
        Project.objects.get_or_create(
            user=user,
            title=project_data['title'],
            defaults=project_data
        )
    
    # Create certifications
    certifications = [
        {
            'name': 'AWS Certified Solutions Architect',
            'issuing_organization': 'Amazon Web Services',
            'issue_date': date(2023, 3, 1),
            'expiry_date': date(2026, 3, 1),
            'credential_id': 'AWS-SAA-123456',
            'credential_url': 'https://aws.amazon.com/verification'
        },
        {
            'name': 'Google Cloud Professional Developer',
            'issuing_organization': 'Google Cloud',
            'issue_date': date(2022, 9, 1),
            'expiry_date': date(2024, 9, 1),
            'credential_id': 'GCP-PD-789012',
            'credential_url': 'https://cloud.google.com/certification'
        }
    ]
    
    for cert_data in certifications:
        Certification.objects.get_or_create(
            user=user,
            name=cert_data['name'],
            defaults=cert_data
        )
    
    # Create technical skills
    skills = [
        {'name': 'Python', 'category': 'programming', 'proficiency': 5},
        {'name': 'JavaScript', 'category': 'programming', 'proficiency': 5},
        {'name': 'TypeScript', 'category': 'programming', 'proficiency': 4},
        {'name': 'Django', 'category': 'framework', 'proficiency': 5},
        {'name': 'React', 'category': 'framework', 'proficiency': 4},
        {'name': 'Vue.js', 'category': 'framework', 'proficiency': 4},
        {'name': 'PostgreSQL', 'category': 'database', 'proficiency': 4},
        {'name': 'MongoDB', 'category': 'database', 'proficiency': 3},
        {'name': 'Docker', 'category': 'tool', 'proficiency': 4},
        {'name': 'AWS', 'category': 'tool', 'proficiency': 4},
    ]
    
    for skill_data in skills:
        TechnicalSkill.objects.get_or_create(
            user=user,
            name=skill_data['name'],
            defaults=skill_data
        )
    
    # Create languages
    languages = [
        {'name': 'English', 'proficiency': 'native'},
        {'name': 'Spanish', 'proficiency': 'intermediate'},
        {'name': 'French', 'proficiency': 'beginner'},
    ]
    
    for lang_data in languages:
        Language.objects.get_or_create(
            user=user,
            name=lang_data['name'],
            defaults=lang_data
        )
    
    # Create sample resume
    resume, created = Resume.objects.get_or_create(
        user=user,
        title='Software Developer Resume',
        defaults={'template': 'modern'}
    )
    
    print(f"Sample data created for user: {user.email}")
    print("Login credentials: john.doe@example.com / testpass123")

if __name__ == '__main__':
    create_sample_user()
    print("Sample data seeding completed!")

#!/bin/bash
echo "Setting up Django Resume Builder..."

# Update pip first
echo "Updating pip..."
python -m pip install --upgrade pip

# Create virtual environment
echo "Creating virtual environment..."
python -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install Django==4.2.7
pip install djangorestframework==3.14.0
pip install django-cors-headers==4.3.1
pip install psycopg2-binary==2.9.7
pip install django-environ==0.11.2
pip install django-filter==23.3
pip install djangorestframework-simplejwt==5.3.0
pip install djoser==2.2.0
pip install drf-spectacular==0.26.5
pip install Pillow==10.0.1
pip install django-allauth==0.57.0
pip install reportlab==4.0.4
pip install python-docx==1.1.0
pip install weasyprint==60.1

echo "Setup completed!"
echo ""
echo "To activate the virtual environment in the future, run:"
echo "source venv/bin/activate"
echo ""
echo "Then you can run:"
echo "python manage.py runserver"

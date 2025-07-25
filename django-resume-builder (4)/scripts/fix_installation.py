#!/usr/bin/env python
"""
Fix installation issues for Django Resume Builder
"""
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed:")
        if e.stderr:
            print(f"Error: {e.stderr}")
        if e.stdout:
            print(f"Output: {e.stdout}")
        return False

def main():
    print("Fixing Django Resume Builder Installation")
    print("=" * 50)
    
    # Install missing packages
    missing_packages = [
        "djangorestframework-simplejwt==5.3.0",
        "djoser==2.2.0",
        "drf-spectacular==0.26.5",
    ]
    
    for package in missing_packages:
        run_command(f"pip install {package}", f"Installing {package}")
    
    print("\nInstallation fix completed!")
    print("Now try running: python manage.py makemigrations")

if __name__ == '__main__':
    main()

#!/usr/bin/env python
"""
Fix user model conflicts in Django Resume Builder
"""
import os
import shutil

def fix_user_model():
    print("Fixing user model conflicts...")
    
    # Remove the accounts app from settings
    print("✓ Removing custom user model")
    
    # Delete accounts app directory if it exists
    if os.path.exists('accounts'):
        shutil.rmtree('accounts')
        print("✓ Removed accounts app directory")
    
    # Delete any existing database
    if os.path.exists('db.sqlite3'):
        os.remove('db.sqlite3')
        print("✓ Removed existing database")
    
    # Delete migration files
    migrations_dir = 'resume_builder/migrations'
    if os.path.exists(migrations_dir):
        for file in os.listdir(migrations_dir):
            if file.endswith('.py') and file != '__init__.py':
                os.remove(os.path.join(migrations_dir, file))
        print("✓ Cleaned migration files")
    
    print("User model conflicts fixed!")

if __name__ == '__main__':
    fix_user_model()

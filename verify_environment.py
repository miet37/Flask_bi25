#!/usr/bin/env python3
"""
Environment verification script for Flask_bi25 on PythonAnywhere
This script checks if all dependencies are properly installed and configured.
"""

import sys
import os

def print_header(text):
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}")

def check_python_version():
    print_header("Checking Python Version")
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    if version.major == 3 and version.minor >= 8:
        print("✓ Python version is compatible")
        return True
    else:
        print("✗ Python 3.8 or higher is required")
        return False

def check_dependencies():
    print_header("Checking Dependencies")
    dependencies = {
        'flask': 'Flask',
        'flask_bootstrap': 'bootstrap-flask',
        'flask_sqlalchemy': 'Flask-SQLAlchemy',
        'numpy': 'numpy',
        'matplotlib': 'matplotlib'
    }
    
    all_ok = True
    for module, package in dependencies.items():
        try:
            __import__(module)
            print(f"✓ {package} is installed")
        except ImportError:
            print(f"✗ {package} is NOT installed")
            print(f"  Install with: pip install {package}")
            all_ok = False
    
    return all_ok

def check_app_structure():
    print_header("Checking Application Structure")
    
    # Get the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    required_paths = {
        'Flask_bi25/app.py': 'Main application file',
        'Flask_bi25/model.py': 'Database models',
        'Flask_bi25/templates': 'Templates directory',
        'Flask_bi25/static': 'Static files directory',
        'Flask_bi25/instance': 'Instance directory (for database)',
    }
    
    all_ok = True
    for path, description in required_paths.items():
        full_path = os.path.join(script_dir, path)
        if os.path.exists(full_path):
            print(f"✓ {description}: {path}")
        else:
            print(f"✗ {description} NOT FOUND: {path}")
            all_ok = False
    
    return all_ok

def check_database():
    print_header("Checking Database Configuration")
    
    try:
        # Change to Flask_bi25 directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        app_dir = os.path.join(script_dir, 'Flask_bi25')
        
        # Add to path if needed
        if app_dir not in sys.path:
            sys.path.insert(0, app_dir)
        
        os.chdir(app_dir)
        
        # Import and test
        from Flask_bi25.app import app, db
        
        with app.app_context():
            # Try to create tables
            db.create_all()
            print("✓ Database can be initialized")
            
            # Check if database file was created
            db_path = os.path.join(app_dir, 'instance', 'att_register.db')
            if os.path.exists(db_path):
                print(f"✓ Database file exists: {db_path}")
            else:
                print(f"✓ Database will be created at: {db_path}")
            
            return True
            
    except Exception as e:
        print(f"✗ Database check failed: {e}")
        return False

def check_imports():
    print_header("Checking Application Imports")
    
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        app_dir = os.path.join(script_dir, 'Flask_bi25')
        
        if app_dir not in sys.path:
            sys.path.insert(0, app_dir)
        
        os.chdir(app_dir)
        
        # Try importing the app
        from Flask_bi25.app import app, db, Attendance
        from Flask_bi25.model import Student
        
        print("✓ Flask application imports successfully")
        print("✓ Database models import successfully")
        
        # Check app config
        print(f"✓ App secret key is set: {'mpRec20813' != app.config['SECRET_KEY']}")
        print(f"✓ Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        
        return True
        
    except Exception as e:
        print(f"✗ Import check failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║  Flask_bi25 Environment Verification Tool                 ║
║  For PythonAnywhere Deployment                            ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    results = []
    
    # Run all checks
    results.append(("Python Version", check_python_version()))
    results.append(("Dependencies", check_dependencies()))
    results.append(("App Structure", check_app_structure()))
    results.append(("App Imports", check_imports()))
    results.append(("Database", check_database()))
    
    # Summary
    print_header("Verification Summary")
    all_passed = True
    for name, passed in results:
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{name:.<40} {status}")
        if not passed:
            all_passed = False
    
    print()
    if all_passed:
        print("🎉 All checks passed! Your environment is ready.")
        print("   You can now configure your PythonAnywhere web app.")
        print("   See PYTHONANYWHERE_SETUP.md for deployment instructions.")
        return 0
    else:
        print("⚠️  Some checks failed. Please fix the issues above.")
        print("   Refer to README.md or PYTHONANYWHERE_SETUP.md for help.")
        return 1

if __name__ == '__main__':
    sys.exit(main())

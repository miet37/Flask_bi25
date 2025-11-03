# WSGI configuration for PythonAnywhere
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/YOUR_USERNAME/Flask_bi25'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Change to the Flask_bi25 subdirectory where app.py is located
os.chdir(os.path.join(project_home, 'Flask_bi25'))

# Import Flask app
from Flask_bi25.app import app as application

# WSGI configuration for PythonAnywhere
import sys
import os

# ⚠️ IMPORTANT: Replace REPLACE_WITH_YOUR_USERNAME with your actual PythonAnywhere username ⚠️
# Example: If your username is 'john_doe', change the line below to:
# project_home = '/home/john_doe/Flask_bi25'
project_home = '/home/REPLACE_WITH_YOUR_USERNAME/Flask_bi25'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Change to the Flask_bi25 subdirectory where app.py is located
flask_app_dir = os.path.join(project_home, 'Flask_bi25')
os.chdir(flask_app_dir)

# Add Flask_bi25 directory to path for imports
if flask_app_dir not in sys.path:
    sys.path.insert(0, flask_app_dir)

# Import Flask app
from app import app as application

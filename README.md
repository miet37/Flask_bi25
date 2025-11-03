# Flask_bi25 - Attendance Tracking Application

A Flask-based web application for tracking student attendance, managing forms, and visualizing data.

## Features

- Student attendance tracking with SQLite database
- Multiple form submission methods (in-memory, CSV, JSON, database)
- Live data visualization with charts
- Admin interface for uploading student CSV files
- Bootstrap-based responsive UI

## PythonAnywhere Deployment

### Prerequisites
- A PythonAnywhere account (free or paid)
- Basic knowledge of Python and Flask

### Step 1: Clone the Repository

1. Log in to your PythonAnywhere account
2. Open a Bash console
3. Clone this repository:
```bash
git clone https://github.com/miet37/Flask_bi25.git
cd Flask_bi25
```

### Step 2: Set Up Virtual Environment

```bash
mkvirtualenv --python=/usr/bin/python3.10 flask_bi25_env
pip install -r requirements.txt
```

### Step 3: Initialize the Database

```bash
cd Flask_bi25
python3 -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### Step 4: Configure Web App on PythonAnywhere

1. Go to the **Web** tab in PythonAnywhere dashboard
2. Click **Add a new web app**
3. Choose **Manual configuration** (not the Flask wizard)
4. Select **Python 3.10** (or your preferred version)
5. Click **Next**

### Step 5: Update WSGI Configuration

1. In the Web tab, find the **Code** section
2. Click on the WSGI configuration file link
3. Replace the content with:

```python
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
```

**Important:** Replace `YOUR_USERNAME` with your actual PythonAnywhere username.

### Step 6: Configure Static Files

In the Web tab, under **Static files**, add:

| URL | Directory |
|-----|-----------|
| /static/ | /home/YOUR_USERNAME/Flask_bi25/Flask_bi25/static/ |

### Step 7: Set Virtual Environment

In the Web tab, under **Virtualenv**, enter:
```
/home/YOUR_USERNAME/.virtualenvs/flask_bi25_env
```

### Step 8: Reload and Test

1. Click the **Reload** button at the top of the Web tab
2. Visit your site at `YOUR_USERNAME.pythonanywhere.com`

## Local Development

To run the application locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
cd Flask_bi25
python app.py
```

The application will be available at `http://127.0.0.1:5000/`

## Project Structure

```
Flask_bi25/
├── Flask_bi25/
│   ├── app.py              # Main Flask application
│   ├── model.py            # Database models
│   ├── static/             # Static files (CSS, images, data)
│   ├── templates/          # HTML templates
│   └── instance/           # Instance folder (database)
├── requirements.txt        # Python dependencies
├── wsgi.py                # WSGI configuration for deployment
└── README.md              # This file
```

## Dependencies

- **Flask** (3.0.0): Web framework
- **Flask-Bootstrap** (2.3.3): Bootstrap integration for Flask
- **Flask-SQLAlchemy** (3.1.1): SQLAlchemy integration for database operations
- **numpy** (1.26.2): Numerical computing for data visualization
- **matplotlib** (3.8.2): Plotting library for charts

## Routes

- `/` - Home page
- `/form1` - Simple form (no persistence)
- `/form2` - Form with CSV/JSON persistence
- `/form3` - Form with database persistence
- `/attendance` - View attendance records
- `/admin/upload_students` - Admin page for uploading student CSV
- `/live_chart` - Live data visualization
- `/chart` - Static chart display
- `/mpl_stat_plot` - Matplotlib scatter plot

## Configuration

Key configuration in `app.py`:
- Database: SQLite (`att_register.db`)
- Secret key: Change in production
- File upload limits: 16MB max
- Bootstrap theme: Sandstone

## Security Notes

- Change the `SECRET_KEY` in `app.py` for production deployment
- Ensure proper file permissions for the database and upload directories
- Consider adding authentication for admin routes

## Troubleshooting

### Database Issues
If you encounter database errors:
```bash
cd Flask_bi25
rm instance/att_register.db
python3 -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### Import Errors
Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Static Files Not Loading
Check that the static files path is correctly configured in PythonAnywhere's Web tab.

## License

This project is for educational purposes.

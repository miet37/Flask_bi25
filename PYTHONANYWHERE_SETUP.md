# PythonAnywhere Quick Start Guide

This guide provides step-by-step instructions for deploying Flask_bi25 on PythonAnywhere with minimal environment setup.

## Quick Setup (5 minutes)

### 1. Clone Repository
```bash
# Open a Bash console on PythonAnywhere
cd ~
git clone https://github.com/miet37/Flask_bi25.git
cd Flask_bi25
```

### 2. Create Virtual Environment
```bash
# Create virtual environment with Python 3.10
mkvirtualenv --python=/usr/bin/python3.10 flask_bi25_env

# Install dependencies (minimal set)
pip install -r requirements.txt
```

### 3. Initialize Database
```bash
cd Flask_bi25
python3 << EOF
from app import app, db
with app.app_context():
    db.create_all()
print("Database initialized successfully!")
EOF
cd ..
```

### 4. Configure Web App

1. Go to PythonAnywhere **Web** tab
2. Click **"Add a new web app"**
3. Choose **"Manual configuration"** (Python 3.10)
4. Click through the wizard

### 5. Edit WSGI File

Click on the WSGI configuration file and replace ALL content with:

```python
import sys
import os

# IMPORTANT: Replace YOUR_USERNAME with your PythonAnywhere username
project_home = '/home/YOUR_USERNAME/Flask_bi25'

if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Change to Flask_bi25 subdirectory and add to path
flask_app_dir = os.path.join(project_home, 'Flask_bi25')
os.chdir(flask_app_dir)

if flask_app_dir not in sys.path:
    sys.path.insert(0, flask_app_dir)

from app import app as application
```

**Remember to replace `YOUR_USERNAME`!**

### 6. Configure Static Files

In the Web tab, add this static file mapping:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/YOUR_USERNAME/Flask_bi25/Flask_bi25/static/` |

### 7. Set Virtual Environment Path

In the Web tab, "Virtualenv" section:
```
/home/YOUR_USERNAME/.virtualenvs/flask_bi25_env
```

### 8. Reload and Access

1. Click green **"Reload"** button
2. Visit: `YOUR_USERNAME.pythonanywhere.com`
3. Done! 🎉

## Minimal Environment Details

This setup uses only these packages:
- **Flask** - Web framework
- **bootstrap-flask** - Bootstrap 5 integration
- **Flask-SQLAlchemy** - Database ORM
- **numpy** - Numerical computing
- **matplotlib** - Charts and plots

Total installation size: ~50-70 MB

## Troubleshooting

### Issue: ImportError for Bootstrap5
**Solution:** Make sure you installed `bootstrap-flask` (not Flask-Bootstrap)
```bash
workon flask_bi25_env
pip install bootstrap-flask
```

### Issue: Database errors
**Solution:** Reinitialize the database
```bash
cd ~/Flask_bi25/Flask_bi25
rm -f instance/att_register.db
python3 -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### Issue: 502 Bad Gateway
**Solution:** Check error log in PythonAnywhere Web tab. Usually means:
- Wrong path in WSGI file
- Missing dependencies
- Python syntax error

### Issue: Static files not loading
**Solution:** Verify static files path in Web tab matches exactly:
```
/home/YOUR_USERNAME/Flask_bi25/Flask_bi25/static/
```

## Configuration for Production

### Change Secret Key
Edit `Flask_bi25/app.py` line 41:
```python
app.config['SECRET_KEY'] = 'your-unique-secret-key-here'
```

### Disable Debug Mode
Edit `Flask_bi25/app.py` line 37:
```python
app.config["DEBUG"] = False
```

Then reload your web app.

## Updating the Application

```bash
cd ~/Flask_bi25
git pull origin main
workon flask_bi25_env
pip install -r requirements.txt --upgrade
# Then click Reload in Web tab
```

## File Structure on PythonAnywhere

```
/home/YOUR_USERNAME/
├── Flask_bi25/                    # Git repository
│   ├── Flask_bi25/               # Application code
│   │   ├── app.py               # Main application
│   │   ├── model.py             # Database models
│   │   ├── static/              # Static files
│   │   ├── templates/           # HTML templates
│   │   └── instance/            # Database (created on first run)
│   ├── requirements.txt         # Dependencies
│   ├── wsgi.py                 # WSGI config template
│   └── README.md               # Full documentation
└── .virtualenvs/
    └── flask_bi25_env/          # Virtual environment
```

## Features Available

Once deployed, you can access:
- **Home page** - Landing page with navigation
- **Forms** - Multiple form submission methods
- **Attendance tracking** - View submitted records
- **Live charts** - Real-time data visualization
- **Admin tools** - Upload student CSV files

## Security Notes for Production

1. Change the SECRET_KEY (see above)
2. Turn off DEBUG mode (see above)
3. Consider adding authentication for `/admin/*` routes
4. Review file upload security in production use
5. Set up regular database backups

## Support

For issues specific to this application, check the main README.md
For PythonAnywhere help, visit: https://help.pythonanywhere.com/

## Performance Optimization Tips

1. **Use SQLite properly**: Already configured for minimal overhead
2. **Static files**: Served directly by PythonAnywhere (no Flask overhead)
3. **Keep dependencies minimal**: Already done in requirements.txt
4. **Consider caching**: For production, add Flask-Caching if needed

## Free Tier Limitations

PythonAnywhere free tier includes:
- ✅ Sufficient for this app
- ✅ Always-on web app
- ⚠️  Limited CPU time/day
- ⚠️  No HTTPS on custom domains (use .pythonanywhere.com)

This application is optimized to work well within free tier limits!

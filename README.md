# STARTING PROJECT
### сreate a virtual environment
*python -m venv venv*

### install all modules
*pip install -r requirements.txt*

### sync your database for the first time:
*python manage.py migrate*
*python manage.py makemigrations*

### create superuser if needed
*python manage.py createsuperuser*

### and run app
*python manage.py runserver*

### enjoy!

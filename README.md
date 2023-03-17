## STARTING PROJECT
### 1. сreate a virtual environment
*python -m venv venv*

### 2. install all packages
*pip install -r requirements.txt*

### *3. sync your database for the first time:
*python manage.py migrate*
*python manage.py makemigrations*

### *4. create superuser if needed to view/update products with admin site
*python manage.py createsuperuser*

### 5. and run app
*python manage.py runserver*

### 6. enjoy!

### *you don`t need these steps if project db.sqlite3 was downloaded from there

### **also you can run tests if you needed by
*python manage.py test menu.tests*

## CHECK THIS OUT
*http://127.0.0.1:8000/api/categories/*

## Filtering product objects is avaliable for 'food__is_vegan' and 'food__is_special' parameters.
## For Example : http://127.0.0.1:8000/api/categories/?food__is_vegan=true&food__is_special=false

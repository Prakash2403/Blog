## HOW TO RUN 

### Requirements:

1. Postgresql should be installed.

2. Go to project directory. Run pip install -r requirements.txt to install python requirememtns.

### Database Settings

Run the following commands in psql console:-

    CREATE DATABASE django_blog;
    CREATE USER django_blog WITH PASSWORD '\<set some password here\>';
    GRANT ALL PRIVILEGES ON DATABASE djangp_blog TO django_blog;
    
### Environment Variables

You have to set three environment variables.

    DB_NAME='django_blog'
    DB_USER='django_blog'
    DB_PASSWORD='<Whatever password you had entered above>'

### Elasticsearch Settings

This is optional, but if you want blog search feature, you have to setup elasticsearch.

    Go to https://www.elastic.co/downloads/elasticsearch
    Download elasticsearch and follow instructions given on that page to run it.
    If elasticsearch is working properly, then uncomment last two lines at /post/apps.py
    If you are facing some problem, then open an issue and post traceback there.   
### Run Web Application

#### Prerequisite
  
    Above two steps must be done.
 
#### How to run the web app
 
    1. Go to project directory (where manage.py is located)
    2. In terminal, type python manage.py makemigrations
    3. If some error is shown in step 2, delete all files except __init__.py in migrations folder of every app.
    4. If still error persists, open an issue and post traceback.
    5. Now run python manage.py migrate
    6. If some error occurs in above step, open an issue and post traceback.
    7. Finally, run python manage.py runserver
    8. Visit 127.0.0.1/8000 and enjoy......
    
    If you want to know about optional arguments, refer to django documentation.

### Managing blog content
    
There are some extra things which needs to be done in order to fully utilize the blog.

    1. Close the application by pressing Ctrl + C.
    2. Run python manage.py createsuperuser.
    3. Follow the instructions and fill required details.
    4. Run python manage.py runserver.
    5. Go to localhost:8000/admin.
    6. Supply required credentials.
    7. Now you can manage the contents of blog.

Note: If you try to access aboutme/ page without filling any entry in About Me section in localhost:8000/admin/, it will show an error. So, make sure that before accessing that page, you fill something about yourself in /admin/ form.

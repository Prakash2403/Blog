# Blogging Platform

## Features

1. Latex support.
2. Markdown support.
3. Multiple file upload via zip folder. Contents get stored in `PROJECT_DIR/media/<post_title>/`
4. Customized search engine powered by elasticsearch.
5. Automatic title image resizing.
6. Disqus support.
7. Draft option for posts which are not completed.
8. Fuzzy search powered by elasticsearch.
9. Separate SECRET_KEY for each user.
10. Settings for `https`, applicable only if your website uses `https`.

 
## Features to add
1. Auto-completion using jQuery autocomplete and elasticsearch completion suggester.
2. Personal commenting engine.


## HOW TO RUN 

### Requirements:

1. Postgresql should be installed.

2. Go to project directory. Run pip install -r requirements.txt to install python requirememtns.

3. User running this project must have rights to read from a file and write to a file within the project
   directory.

### Database Settings

Run the following commands in psql console:-

    CREATE DATABASE django_blog;
    CREATE USER django_blog WITH PASSWORD '\<set some password here\>';
    GRANT ALL PRIVILEGES ON DATABASE django_blog TO django_blog;
    
### Environment Variables

You have to set four environment variables.

    DB_NAME='django_blog'
    DB_USER='django_blog'
    DB_PASSWORD='<Whatever password you had entered above>'
    ELASTICSEARCH_ENABLED = True
    BLOG_SECRET_KEY = <Generate a secret key for your server>


### Elasticsearch Settings

    Go to https://www.elastic.co/downloads/elasticsearch
    Download elasticsearch and follow instructions given on that page to run it.

Sometimes, your system may lag when you run elasticsearch. This is because default memory allocated to elasticsearch is 
2GB. So, if you are facing this problem, open config/jvm.options and set -Xms and -Xmx values to 512m. If still it lags,
lower down the values to 256m. Make sure that Xms and Xmx values are same.

If you want to turn off the search feature due to some reason, then set `ELASTICSEARCH_ENABLED=False`

If you are facing some problem, then open an issue and post traceback there.   


#### Prerequisite
  
    There should be no error in above steps.
 
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
    
There are some extra things which needs to be done in order to manage the blog.

    1. Create a super user by running python manage.py createsuperuser.
    2. Go to localhost:8000/admin.
    3. Supply required credentials.
    4. Now you can manage the contents of blog.

Note: If you try to access aboutme/ page without filling any entry in About Me section in localhost:8000/admin/, 
it will show an error. So, make sure that before accessing that page, you fill something about yourself in /admin/ 
form.

## TODOS

1. Follow software engineering principles to enhance the code.
2. Enhance the front end.
3. Documentation of existing code.

## Contributions

Following points should be kept in mind while submitting a PR.
1. Coding guidelines for languages must be followed.
2. Code must be documented properly, and format of docstrings must be in standard 
format for that language.
3. PR title must be descriptive. It is advised to create an issue before submitting a PR and then 
refer that issue while making the PR.

## Demo

Click [here](http://techalert.me) for demo.

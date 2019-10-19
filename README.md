<p align="center"> 
<img src="../master/images/logo.png">
</p>

<p align="center">Flask-Now is a Flask Application Generator/Build-Tool runs via CLI</p> 

## What is Flask-Now
Since Flask is commonly used in kickstarting a project, developers shouldn't waste their time with creating folders like static/css, static/js, configuration, controllers, models etc. Aim of Flask-Now is __*auto generating necessity folders and files according to your architectural pattern and semi-automatically installing desired flask extension*__. Since Flask is very flexible microframework, it may fit many architectural pattern. Currently following patterns can be auto generated using Flask-Now:

### Supported Patterns
Flask-Now supports two different patterns:

#### simple
- It is a very simple flask application structure for very small applications
```
/your_project_folder
    venv
    run.py
    config.py
    models.py
    requirements.txt
```

#### bp (Known as blueprints)
- As suggested in [official tutorial](https://flask.palletsprojects.com/en/1.1.x/blueprints/), Flask Now has a similar folder structure which is called as bp:
```

/your_project_folder
    venv
    run.py
    requirements.txt
    /project
        __init__.py
        /blueprints
            /index -> an example blueprint
                __init__.py
                controller.py
                forms.py  
        models.py
        config.py
        /static
            /css
                style.css
            /js
                script.js
        /templates
            index.html
```

## How to use

#### Requirements
- Python 3.x
- Virtualenvironment
- pip3

Let me explain this project with an example. Assume that we want to create an Flask Application called ```flaskr```

### GNU/Linux - OSX

#### Install
- Install flask-now with pip to your global environment, this will add an executable file to your /bin with the name flask-now which is the runnable application:
```
sudo pip3 install flask-now
```
#### Usage
- Go to the folder you wish to create the project:
```
cd my_development_folder
```
- Create the app! Let's assume that we want to create an app named 'flaskr' with simple pattern with flask-wtf and flask-sqlalchemy installed

```
flask-now flaskr simple -e sqlalchemy wtf

```
- That's it. Now activate the virtualenv and run the project:
```
cd flaskr && source/venv/bin/activate && python run.py
```
- As you can understand from the example we drop Flask keyword while installing flask extensions to our project.

- Some examples which may confuse you:
  - Flask-Rest-Jsonapi -> rest-jsonapi
  - Frozen-Flask -> frozen

### Uninstall
To uninstall :
```sudo pip3 uninstall flask-now```
## TODO

- Adding more architectural patterns.
- Adding more options for configuration file.
- Adding smart code generation according to desired extensions.(for example if you install Flask-SqlAlchemy, sample model, imports and db configurations will be ready)


## RoadMap
- Generate architecture for rest api's via using [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/) planned version: 0.3.0. New architectural pattern :+1:
- Adding flask-admin via using [Flask-Admin](https://flask-admin.readthedocs.io/en/latest/) planned version: 0.4.0. New architectural pattern :+1:
- Decide if application will be renamed as flask-up, maybe both will be used while calling from console. [Naming proposal](https://github.com/ozanonurtek/flask-now/issues/5) which is started under [this reddit post](https://www.reddit.com/r/flask/comments/ddtprp/flasknow_flask_app_generator_v021/). Not planned yet.

## ChangeLog

- 0.2.1 project recreated.
- 0.2.2 
    - Thanks to [this issue](https://github.com/ozanonurtek/flask-now/pull/6) which is created by [c-w](https://github.com/c-w), flask-now perfectly works on Windows. :clap:
    - RoadMap and ChangeLog added.
    - Minor addition: flask-now waits for confirmation to create your project if given project name exists as folder. 


## Contribution

Please feel free to contribute to this project, open issues, fork it, send pull requests.

You can also send email to my mail adress.__ozanonurtek@gmail.com__

Happy coding :metal:

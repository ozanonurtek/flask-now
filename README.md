# Flask-Now
A simple Flask Application Generator runs via CLI. 

## What is Flask-Now
Since Flask is commonly used in kickstarting a project, developers shouldn't waste their time with creating folders like static/css, static/js, configuration, controllers, models etc. Aim of Flask-Now is __*auto generating necessity folders and files according to your architectural pattern and semi-automatically installing desired [flask extensions](http://flask.pocoo.org/extensions/)*__. Since Flask is very flexible microframework, it may fit many architectural pattern. Currently following patterns can be auto generated using Flask-Now:

### Supported Patterns
Flask-Now supports two different patterns:

#### simple
- It is a very simple flask application structure for very small applications
```
/your_project_folder
    venv
    run.py
    config.py
    requirements.txt
```

#### mvc
- As suggested in [official tutorial](http://flask.pocoo.org/docs/0.12/tutorial/folders/), Flask Now has a similar folder structure which is called as MVC:
```

/your_project_folder
    venv
    run.py
    requirements.txt
    /project
        __init__.py
        controller.py
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

### Supported Flask Extensions
You can auto-install following Flask Extensions while building your architecture:
[List of Extensions](http://flask.pocoo.org/extensions/)

Also supports:
- Flask-Bootstrap

## How to use

#### Requirements
- Python 3.x
- Virtualenvironment
- pip3

Let me explain this project with an example. Assume that we want to create an Flask Application called ```flaskr```

### GNU/Linux - OSX

#### Install

- Create a project folder:
```
mkdir flaskr && cd flaskr
```
- Setup a virtualenvironment:
```
virtualenv -p python3 venv
```
- Activate it:
```
source venv/bin/activate
```
- Install flask-now with pip, this will also install flask(flask is requirement of flask-now):
```
pip install flask-now
```

#### Usage

- Create a py file in flaskr's root directory and let's call it build.py
```
nano build.py
```
- Now insert following 2 lines of code into build.py file:
```
import flask_now
flask_now.build()
```
- **Important part starts**, we will run this build.py with command line arguments, let's assume that we need Flask-WTF and Flask-Bootstrap in MVC patern:
```
python3 build.py -mvc wtf bootstrap
```
If you run the code above, Flask-Now will do the all job for you.


- If you want to create a *simple structure* that I mentioned above, don't pass architecture pattern(```-mvc```) arguments to build.py. Example:
```
python3 build.py wtf bootstrap
```
- As you can understand from the example we drop Flask keyword while installing flask extensions to our project. For example:

If we want to install *Flask-Admin*, **we just drop Flask keyword at the beginning of the extension** and passing *admin* as an argument to build.py.

Some examples which may confuse you:

Flask-Rest-Jsonapi -> rest-jsonapi

Frozen-Flask -> frozen
```
python3 build.py -mvc frozen rest-jsonapi wtf bootstrap admin
```
And that's it. Your simple flask app is ready. Run it!
```
python3 run.py
```
This application initially have 3 configuration objects in ```config.py```:

```DEBUG=True```

```SECRET_KEY```= It is generated automatically as suggested in(using ```os.urandom()```) [Flask Quick Start](http://flask.pocoo.org/docs/0.12/quickstart/)

```SERVER_NAME="127.0.0.1:5000```

## TODO

- Adding more architectural patterns.
- Adding more options for configuration file.
- Adding smart code generation according to desired extensions.(for example if you install Flask-SqlAlchemy, sample model, imports and db configurations will be ready)

## Contribution

Please feel free to contribute to this project, open issues, fork it, send pull requests.

If your flask extension does not included in this software please feel free to send me an email.

You can also send email to my mail adress.__ozanonurtek@gmail.com__

Happy coding :metal:

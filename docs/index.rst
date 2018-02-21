===========================================
Flask-Now
===========================================

Overview
================

Welcome to `flask-now 0.1.5`_ documentation. Flask-Now is a simple command line interface tool which can generate the architectural pattern, folder structures and flask extensions for your project.

.. _flask-now 0.1.5: https://pypi.python.org/pypi/flask-now/0.1.5


Goal
================

The aim of Flask-Now is auto-generating necessity folders and files according to your architectural pattern and semi-automatically installing desired `flask extensions`_.


So, just concentrate on application logic, Flask-Now is at your services :)

.. _flask extensions: http://flask.pocoo.org/extensions/

Quick-Start
================

Requirements
------------

- Python 3.x
- Virtualenvironment
- pip3

Installing(GNU/Linux - OSX)
----------
Install flask-now with pip, this will add an executable file to your /bin with the name flask-now which is out application

.. code-block:: bash

  pip install --user flask-now

Usage
----------

Now go to your project folder, create your virtualenvironment, activate it and build your project with your favourite flask extensions and architectural pattern

.. code-block:: bash

  flask-now -mvc wtf bootstrap sqlalchemy

That's it, your project is ready in a minute with desired flask extensions and with following mvc like architectural pattern,

.. code-block:: python

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

which has a very similar folder structure as suggested in `official tutorial`_.

.. _official tutorial: http://flask.pocoo.org/docs/0.12/tutorial/folders/

Parameter Passing
=================

Flask-Now accepts parameters within following structure:

.. code-block:: bash

  flask-now -<architectural-pattern> <extension_1> <extension_2> ... <extension_n>

Which means that you can pass one parameter only as :code:`-<architectural-pattern>`. If you pass more than one architectural-pattern parameters like in the following example:

.. code-block:: bash

  flask-now -mvc -mvvm -simple

Flask-Now will use the latest parameter(in this case it will use :code:`simple`) that you passed as architectural-pattern.

If no parameter is passed to Flask-Now, it will build a simple architecture with no extension:

.. code-block:: bash

  flask-now

which will produce a Flask ready project with following folder structure:

.. code-block:: python

  /your_project_folder
    venv
    run.py
    config.py
    requirements.txt

It is a very simple Flask Application and of course, it is ready to run!

.. code-block:: python

  python3 run.py

Supported Architectural Patterns
================================

Flask-Now supports two type of patterns in this version, more patterns will be added in next releases.


simple
----------

Running:

.. code-block:: bash

  flask-now -simple

With :code:`-simple` parameter, Flask-Now will generate very simple Flask Application with in following structure:

.. code-block:: python

  /your_project_folder
    venv
    run.py
    config.py
    requirements.txt

- If you don't pass any parameter as :code:`architectural-pattern` Flask-Now will build a :code:`simple` folder structure for your project:

.. code-block:: bash

  flask-now

is the exact same thing with:

.. code-block:: bash

  flask-now -simple

mvc
------------

Running:

.. code-block:: bash

  flask-now -mvc

With :code:`-mvc` parameter, Flask-Now will generate very similar Flask Application which is suggested in `official tutorial`_.

.. _official tutorial: http://flask.pocoo.org/docs/0.12/tutorial/folders/


.. code-block:: python

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

Supported Flask-Extensions
==========================

Flask-Now supports all `official extensions`_. You can build your Flask Application with extensions using following rule:

.. _official extensions: http://flask.pocoo.org/extensions/

Generally, Flask Extensions are named as follows:

.. code-block:: Python

  Flask-SQLAlchemy
  Flask-Themes
  Flask-WTF
  etc...

Which means that they have following pattern:

.. code-block:: Python

  Flask-<extension-name>

except:

.. code-block:: Python

  Frozen-Flask

So you just need to drop **Flask-** or **-Flask** keyword from the name of the extension. For example, if you wish to use :code:`Flask-WTF`, :code:`Frozen-Flask`, :code:`Flask-Static-Compress` and :code:`Flask-SQLAlchemy` in your project with mvc like architecture, you just need to run flask-now as follows:

.. code-block:: bash

  flask-now -mvc frozen wtf static-compress sqlalchemy

That's it, Flask-Now will build your Flask Application with desired extensions and mvc like pattern! :code:`requirements.txt, config.py` is also at your services!

You just have to do

.. code-block:: Python

  python3 run.py

Initial Content Of Files
========================

config.py
---------

Initially, content of :code:`config.py` as follows:

.. code-block:: Python

  DEBUG=True
  SECRET_KEY="Ug1cHqJJhRrLHqwqXS56lKh4z977sHqbdJZF3Zdhknrv/ato82t3RZ3nMwsy8Q3wN34ukRPYxhflq3e81gUgSw=="
  SERVER_NAME="127.0.0.1:5000"

When Flask-Now generates :code:`config.py`, it uses :code:`os.urandom()` to generate :code:`SECRET_KEY` as suggested in `flask quick start`_.

.. _flask quick start: http://flask.pocoo.org/docs/0.12/quickstart/

run.py
----------

If it is built with :code:`-simple` parameter, content of :code:`run.py` as follows:

.. code-block:: Python

  from flask import Flask

  app = Flask(__name__)
  app.config.from_pyfile("config.py")


  @app.route("/")
  def index():
    return "<h1>Hello World!</h1>"

  if __name__ == "__main__":
    app.run()

if it is built with :code:`-mvc` parameter, content of :code:`run.py` as follows:

.. code-block:: Python

  from project import app

  if __name__ == "__main__":
    app.run()


requirements.txt
----------------

Flask-Now uses :code:`pip freeze` feature to create latest version of :code:`requirements.txt` file. So, if your run

.. code-block:: bash

  flask-now -simple

Flask-Now will generate following requirements.txt for you:

.. code-block:: Python

  click==6.7
  Flask==0.12.2
  itsdangerous==0.24
  Jinja2==2.10
  MarkupSafe==1.0
  pkg-resources==0.0.0
  Werkzeug==0.14.1

Following files are only available with mvc like architecture:

__init__.py
-------------

.. code-block:: Python

  from flask import Flask, render_template

  app = Flask(__name__)
  app.config.from_pyfile("config.py")


  from project import controller


controller.py
-------------

.. code-block:: Python

  from project import app, render_template

  @app.route("/")
  def index():
      return render_template("index.html")


models.py
-------------

.. code-block:: Python

  # Your models here.


templates/index.html
-------------

.. code-block:: html

  <h1>Flask is fun.</h1>

static/css/style.css
-------------

This file is initially empty.


static/js/script.js
-------------

This file is initially empty.

Uninstalling
=============

Deactivate your virtualenvironment, than:

.. code-block:: bash

  pip uninstall flask-now

Detailed Example
==============

Assume that we want to start a new Flask Application called :code:`flaskr` in current directory.

- Let's install Flask-Now first.

.. code-block:: bash

  pip install --user flask-now

- After installation succeed, let's create our directory for project and go to that directory

.. code-block:: bash

  mkdir flaskr && cd flaskr

- Let's create our virtualenvironment in flaskr directory

.. code-block:: bash

  virtualenv -p python3 venv

- Activate our virtualenvironment

.. code-block:: bash

  source venv/bin/activate

- Finally, build our project using Flask-Now

.. code-block:: bash

  pip install -mvc -wtf -sqlalchemy -login

That's it, you are ready to develop your Flask Application!

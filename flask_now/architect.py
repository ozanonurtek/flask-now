import os, base64


class ArchitectException(Exception):
    pass

class Architect(object):
    def __init__(self, architecture):
        self.__architecture = architecture
        self.__indent = "    "

    def __identify(self):
        if self.__architecture.lower() == "mvc":
            self.__create_mvc_architecture()

        else:
            self.__create_simple_app()

    def __create_mvc_architecture(self):
        self.__create_mvc_app()

    def __create_simple_app(self):
        self.__create_config_file("config.py")
        self.__create_simple_run()



    def __create_config_file(self, filename):
        if self.__architecture == "mvc":
            os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w+") as file:
            try:
                random_bytes = os.urandom(64)
                token = base64.b64encode(random_bytes).decode('utf-8')
                file.write("DEBUG=True\n")
                file.write("SECRET_KEY=" + '"' + token + '"\n')
                file.write('SERVER_NAME="127.0.0.1:5000"\n')
            except:
                raise ArchitectException("Error while creating config.py")


    def __create_mvc_app(self):
        # Create config file
        self.__create_config_file(filename="project/config.py")
        with open("run.py", "w+") as file:
            try:
                file.write("from project import app\n\n")
                file.write('if __name__ == "__main__":\n')
                file.write(self.__indent + "app.run()\n")
            except:
                raise ArchitectException("Error while creating run.py")
        # Create init file
        filename = "project/__init__.py"
        with open(filename, "w+") as file:
            file.write("from flask import Flask, render_template\n\n")
            file.write("app = Flask(__name__)\n")
            file.write('app.config.from_pyfile("config.py")\n\n\n')
            file.write('from project import controller\n')

        # Create simple controller
        filename = "project/controller.py"
        with open(filename, "w+") as file:
            file.write('from project import app, render_template\n\n')
            file.write('@app.route("/")\n')
            file.write("def index():\n")
            file.write(self.__indent + 'return render_template("index.html")\n\n')

        filename = "project/models.py"
        with open(filename, "w+") as file:
            file.write('# Your models here.\n')

        # Create static/css
        filename = "project/static/css/style.css"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w+") as file:
            file.write('\n')

        # Create static/js
        filename = "project/static/js/script.js"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w+") as file:
            file.write('\n')

        # Create a simple template
        filename = "project/templates/index.html"
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "w+") as file:
            file.write('<h1>Flask is fun.</h1>')



    def __create_simple_run(self):
        with open("run.py", "w+") as file:
            try:
                file.write("from flask import Flask\n\n")
                file.write("app = Flask(__name__)\n")
                file.write('app.config.from_pyfile("config.py")\n\n\n')
                file.write('@app.route("/")\n')
                file.write("def index():\n")
                file.write(self.__indent + 'return "<h1>Hello World!</h1>"\n\n')
                file.write('if __name__ == "__main__":\n')
                file.write(self.__indent + "app.run()\n")
            except:
                raise ArchitectException("Error while creating run.py")


    def build(self):
        self.__identify()

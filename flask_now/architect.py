import os, base64


class ArchitectException(Exception):
    pass

class Architect(object):
    def __init__(self, architecture):
        self.__architecture = architecture
        self.__indent = "    "

    def __identify(self):
        if self.__architecture.lower() is "mvc":
            pass
            #self.__create_mvc_architecture()
        elif self.__architecture.lower is "mvvmr":
            pass
            #self.__create_mvvmr_achitecture()
        else:
            self.__create_simple_app()

    def __create_simple_app(self):
        self.__create_config_file()
        self.__create_simple_run()


    def __create_config_file(self):
        with open("config.py", "w+") as file:
            try:
                random_bytes = os.urandom(64)
                token = base64.b64encode(random_bytes).decode('utf-8')
                file.write("DEBUG=True\n")
                file.write("SECRET_KEY=" + '"' + token + '"\n')
                file.write('SERVER_NAME="127.0.0.1:5000"\n')
            except:
                raise ArchitectException("Error while creating config.py")

    def __create_simple_run(self):
        with open("run.py", "w+") as file:
            try:
                file.write("from flask import Flask\n\n")
                file.write("app = Flask(__name__)\n")
                file.write('app.config.from_pyfile("config.py")\n\n\n')
                file.write('@app.route("/")\n')
                file.write("def index():\n")
                file.write(self.__indent + 'return "Hello World!"\n\n')
                file.write('if __name__ == "__main__":\n')
                file.write(self.__indent + "app.run()\n")
            except:
                raise ArchitectException("Error while creating run.py")

    def build(self):
        self.__identify()

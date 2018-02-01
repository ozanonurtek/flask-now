import os, sys, subprocess

class ParserException(Exception):
    pass

class Parser(object):

    def __init__(self):
        self.sys = sys
        self.CREATE_VENV = "virtualenv --python=python3 venv"
        self.ACTIVATE_VENV = "source venv/bin/activate"
        self.__subprocess = subprocess
        self.__package_list = []
        self.__valid_packages = ["wtf", "bootstrap", "sqlalchemy", "user", "uploads", "frozen",
                               "migrate", "login", "assets", "security", "themes",
                               "super-admin", "restless", "restfull", "rest-json"
                               "admin", "oauth", "api", "api-utils",
                               "less-css", "mail", "mako", "misaka", "pymongo"]

    def __read_package_list(self):
        if len(self.sys.argv) > 0:
            for package in self.sys.argv:
                self.__package_list.append(package)


    def __validate_packages(self):
        self.__package_list.remove("now.py")
        if len(self.__package_list) > 0:
            print("No extension will be added. Just creating a extensionless flask app")
        for package in self.__package_list:
            if not package in self.__valid_packages:
                raise ParserException("There is no extension called: " + str(package) + " in now-flask.")


    def __create_requirements(self):
        try:
            with open("requirements.txt", "a") as file:
                for package in self.__package_list:
                    file.write("pip install flask-" + package + "\n")

        except:
            raise ParserException("Cannot create or open: requirements.txt file")

    def __wrap_venv(self):
        process = self.__subprocess.Popen(self.CREATE_VENV, shell=True, stdout=self.__subprocess.PIPE)
        print("Waiting for virtualenv...")
        process.wait()

        if process.returncode == 0:
            print("Virtualenv is created.")
        else:
            print("An error occured while creating virtualenv\nError:\n", process.stdout)


    # WTF BASH
    def __activate_venv(self):
        actual_venv = "source " + str(os.getcwd()) + "/venv/bin/activate"
        print(actual_venv)
        self.__subprocess.Popen([actual_venv], shell=True).wait()

    def parse(self):
        self.__read_package_list()
        self.__validate_packages()
        self.__create_requirements()
        self.__wrap_venv()
        self.__activate_venv()
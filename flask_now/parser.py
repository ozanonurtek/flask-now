# -*- coding: utf-8 -*-

import sys, subprocess

class ParserException(Exception):
    pass

class Parser(object):

    def __init__(self):
        self.__process_result = False
        self.__architecture = ""
        self.__package_list = []
        self.__valid_packages = ["admin","ask","assets","autoindex","babel", "bootstrap","bcrypt","cache","celery","classy","cors",
                                 "couchdb","couchdbkit","creole","dance","dashed","debugtoolbar","exceptional","filling",
                                 "flatpages","fluiddb","gae-mini-profiler","genshi","gravatar","heroku","htmlbuilder",
                                 "lesscss","lettuce","limiter","login","mail","mako","migrate","misaka","mongoalchemy",
                                 "mongokit","oauth","openid","pewee","ponywhoosh","principal","pymongo","queryinspect",
                                 "raptor","rest-jsonapi","restful","restless","script","seasurf","security","shelve",
                                 "sijax","sqlalchemy","sse","static-compress","stormpath","testing","themes","uploads",
                                 "user","via","weasyprint","webtest","wtf","xml-rpc","zen","zodb","frozen"]

    def __read_package_list(self):
        if len(sys.argv) > 0:
            for package in sys.argv:
                if package[0] == "-":
                    self.__architecture = package[1:]
                else:
                    self.__package_list.append(package)

            self.__process_result=True


    def __validate_packages(self):
        self.__package_list.remove(sys.argv[0])
        if self.__architecture == "":
            self.__process_result = True
            if len(self.__package_list) == 0 :
                print("No extension will be added. Just creating a simple, extensionless flask app")
            else:
                print("Creating simple app with following extensions: ", str(self.__package_list))
        elif self.__architecture != "":
            self.__process_result = True
            if len(self.__package_list) == 0:
                print("Creating extensionless flask app with " + self.__architecture + " architecture pattern.")
            else:
                print("Creating flask app with " + self.__architecture + " architecture pattern and with following extensions " + str(self.__package_list))


        for package in self.__package_list:
            if not package in self.__valid_packages:
                self.__process_result=False
                raise ParserException("There is no extension called: " + str(package) + " in now-flask.")


    def __create_requirements(self):
        try:
            with open("requirements.txt", "a") as file:
                file.write("flask\n")
                for package in self.__package_list:
                    if package == "frozen":
                        file.write("frozen-flask \n")
                    else:
                        file.write("flask-" + package + "\n")

            self.__package_list.append("flask")
            self.__process_result = True
        except:
            self.__process_result = False
            raise ParserException("Cannot create or open: requirements.txt file")


    def __install_requirements(self):
        if len(self.__package_list) > 0:
            process = subprocess.Popen("pip install -r requirements.txt", shell=True, stdout=subprocess.PIPE)
            print("Installing requirements...")
            process.wait()
            if process.returncode == 0:
                self.__process_result = True
                process = subprocess.Popen("pip freeze > requirements.txt", shell=True, stdout=subprocess.PIPE)
                print("Freezing requirements...")
                process.wait()
                if process.returncode == 0:
                    self.__process_result = True
                else:
                    print("An error occured while freezing requirements\nError:\n", process.stdout)
                    print("You can manually freeze installed requirements by using following command: 'pip freeze > requirements.txt'")
            else:
                self.__process_result = False
                print("An error occured while installing requirements\nError:\n", process.stdout)
        else:
            self.__process_result = True

    def parse(self):
        self.__read_package_list()
        self.__validate_packages()
        self.__create_requirements()
        self.__install_requirements()

        return self.__process_result, self.__architecture

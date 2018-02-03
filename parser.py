# -*- coding: utf-8 -*-

import sys, subprocess

class ParserException(Exception):
    pass

class Parser(object):

    def __init__(self):
        self.sys = sys
        self.__process_result = False
        self.CREATE_VENV = "virtualenv --python=python3 venv"
        self.__subprocess = subprocess
        self.__package_list = []
        self.__valid_packages = ["admin","ask","assets","autoindex","babel","bcrypt","cache","celery","classy","cors",
                                 "couchdb","couchdbkit","creole","dance","dashed","debugtoolbar","exceptional","filling",
                                 "flatpages","fluiddb","gae-mini-profiler","genshi","gravatar","heroku","htmlbuilder",
                                 "lesscss","lettuce","limiter","login","mail","mako","migrate","misaka","mongoalchemy",
                                 "mongokit","oauth","openid","pewee","ponywhoosh","principal","pymongo","queryinspect",
                                 "raptor","rest-jsonapi","restful","restless","script","seasurf","security","shelve",
                                 "sijax","sqlalchemy","sse","static-compress","stormpath","testing","themes","uploads",
                                 "user","via","weasyprint","webtest","wtf","xml-rpc","zen","zodb","frozen-flask"]

    def __read_package_list(self):
        if len(self.sys.argv) > 0:
            for package in self.sys.argv:
                self.__package_list.append(package)

            self.__process_result=True


    def __validate_packages(self):
        self.__package_list.remove("now.py")
        if len(self.__package_list) == 0:
            print("No extension will be added. Just creating a extensionless flask app")
            self.__process_result=True
        for package in self.__package_list:
            if not package in self.__valid_packages:
                self.__process_result=False
                raise ParserException("There is no extension called: " + str(package) + " in now-flask.")


    def __create_requirements(self):
        try:
            with open("requirements.txt", "a") as file:
                for package in self.__package_list:
                    if package is "frozen-flask":
                        file.write("frozen-flask \n")
                    else:
                        file.write("flask-" + package)
            self.__process_result = True

        except:
            self.__process_result = False
            raise ParserException("Cannot create or open: requirements.txt file")


    def __wrap_venv(self):
        process = self.__subprocess.Popen(self.CREATE_VENV, shell=True, stdout=self.__subprocess.PIPE)
        print("Waiting for virtualenv...")
        process.wait()

        if process.returncode == 0:
            self.__process_result = True
            print("Virtualenv is created.")
        else:
            self.__process_result = False
            print("An error occured while creating virtualenv\nError:\n", process.stdout)


    def parse(self):
        self.__read_package_list()
        self.__validate_packages()
        self.__wrap_venv()
        self.__create_requirements()

        return self.__process_result
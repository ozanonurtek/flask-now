import argparse
import subprocess
import shutil
import sys
import os
import time
import pkg_resources


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='Name of your project', type=str)
    parser.add_argument('--type', help='Type of project: Either Simple or Blueprints: (simple or bp), simple is by default selected',type=str)
    parser.add_argument('-e', '--extensions', help='list of extensions', nargs='+')
    parser.add_argument('-p', '--python', help='Global python3 path', default=sys.executable)

    args = parser.parse_args()

    create_example_app(args.name, args.type)
    create_venv(args.python)
    create_requirements(args.extensions)
    install_extensions()


def create_venv(global_python_path):
    print('{} -m venv venv'.format(global_python_path))
    process = subprocess.Popen('{} -m venv venv'.format(global_python_path), shell=True, stdout=subprocess.PIPE)
    print('Creating virtualenvironment')
    process.wait()
    if process.returncode == 0:
        print('Virtualenvironment created.')
    else:
        print('Virtualenvironment creation failed: {}'.format(process.stdout))


def create_example_app(app_name, app_type=None):
    directory_name = pkg_resources.get_distribution('flask-now').location
    boilerplate_code = {"bp":f'{directory_name}/flask_now/templates/blueprints',"simple":f'{directory_name}/flask_now/templates/simple'}
    try:
        if os.path.isdir(app_name):
            are_you_sure = input(
                'Application named {} already exists. Flask-Now will recreate all files, do you want to continue?(y/n)'.format(
                    app_name))
            if are_you_sure != 'y' and are_you_sure != 'Y':
                print('Flask-Now stopped due to given answer: {}'.format(are_you_sure))
                sys.exit(0)
            shutil.rmtree(app_name)
        shutil.copytree(boilerplate_code.get(app_type,'simple'), app_name)
        os.chdir(app_name)
    except Exception as ex:
        print(ex)


def create_requirements(extensions):
    try:
        print('Creating requirements...')
        with open('requirements.txt', 'a') as file:
            file.write('flask\n')
            if extensions:
                for extension in extensions:
                    if extension == 'frozen':
                        file.write('frozen-flask \n')
                    else:
                        file.write('flask-' + extension + '\n')
        print('Requirements are created.')
    except Exception as ex:
        print('Requirements creation failed')
        print(ex)


def install_extensions():
    if os.name == 'nt':
        pip = os.path.join('venv', 'Scripts', 'pip')
    else:
        pip = os.path.join('venv', 'bin', 'pip')

    print('Intalling extensions...')
    process = subprocess.Popen('{} install -r requirements.txt'.format(pip), shell=True,
                               stdout=subprocess.PIPE)
    while process.poll() is None:
        print(process.stdout.readline().decode('utf-8'))
        time.sleep(0.1)
    process.wait()
    if process.returncode == 0:
        print('Successfuly installed extensions.')
    else:
        print('Could not install extensions: {}'.format(process.stdout))

    process = subprocess.Popen('{} freeze > requirements.txt'.format(pip), shell=True,
                               stdout=subprocess.PIPE)
    print('Freezing requirements...')
    process.wait()
    if process.returncode != 0:
        print('An error occured while freezing requirements\nError:\n', process.stdout)
        print(
            'You can manually freeze installed requirements by using following command: "pip freeze > requirements.txt"')

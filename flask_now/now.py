import argparse
import subprocess
import shutil
import os
import time
import pkg_resources


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='Name of your project', type=str)
    parser.add_argument('type', help='Type of project: Either Simple or Blueprints: (simple or bp)', type=str)
    parser.add_argument('-e', '--extensions', help='list of extensions', nargs='+')
    parser.add_argument('-p', '--python', help='Global python3 path', default='python3')

    args = parser.parse_args()
    global_python = args.python
    if args.python == 'python3':
        process = subprocess.Popen(['which', 'python3'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        out, err = process.communicate()
        code = process.returncode
        if code == 0:
            global_python = out.decode("utf-8")
            global_python = global_python.replace('\n', ' ')
        else:
            raise Exception('No python path supplied: {}'.format(err))

    create_example_app(args.name, args.type)
    create_venv(global_python)
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


def create_example_app(app_name, app_type):
    directory_name = pkg_resources.get_distribution('flask-now').location
    if app_type == 'bp':
        src = '{}/flask_now/templates/blueprints'.format(directory_name)
    if app_type == 'simple':
        src = '{}/flask_now/templates/simple'.format(directory_name)
    try:
        if os.path.isdir(app_name):
            shutil.rmtree(app_name)
        shutil.copytree(src, app_name)
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
    print('Intalling extensions...')
    process = subprocess.Popen('venv/bin/pip install -r requirements.txt', shell=True,
                               stdout=subprocess.PIPE)
    while process.poll() is None:
        print(process.stdout.readline().decode('utf-8'))
        time.sleep(0.1)
    process.wait()
    if process.returncode == 0:
        print('Successfuly installed extensions.')
    else:
        print('Could not install extensions: {}'.format(process.stdout))

    process = subprocess.Popen('venv/bin/pip freeze > requirements.txt', shell=True,
                               stdout=subprocess.PIPE)
    print('Freezing requirements...')
    process.wait()
    if process.returncode != 0:
        print('An error occured while freezing requirements\nError:\n', process.stdout)
        print(
            'You can manually freeze installed requirements by using following command: "pip freeze > requirements.txt"')

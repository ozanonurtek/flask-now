from setuptools import setup

setup(name='flask-now',
      version='0.1',
      description='Flask App Generator',
      url='http://github.com/ozanonurtek/flask-now',
      author='Ozan Onur Tek',
      author_email='ozanonurtek@gmail.com',
      license='GPLv3',
      install_requires=[
          'flask'
      ],
      packages=['flask_now'],
      zip_safe=False)

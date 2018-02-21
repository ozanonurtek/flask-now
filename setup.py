from setuptools import setup


def readme():
    with open('README.rst') as readme:
        return readme.read()


setup(name='flask-now',
      version='0.1.5',
      description='Flask App Generator',
      long_description=readme(),
      classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Code Generators',
        'Development Status :: 3 - Alpha',
        'Framework :: Flask',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3 :: Only',
      ],
      keywords='extension flask flask-extension build-tool flask-build-tool flask_now flask-now app-generator flask-app-generator app generator',
      url='http://github.com/ozanonurtek/flask-now',
      author='Ozan Onur Tek',
      author_email='ozanonurtek@gmail.com',
      packages=['flask_now'],
      entry_points = {'console_scripts': ['flask-now = flask_now.now:main']},
      include_package_data=True,
      zip_safe=False)

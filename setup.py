from setuptools import setup


def readme():
    with open('README.rst') as readme:
        return readme.read()


setup(name='flask-now',
      version='0.1.3',
      description='Flask App Generator',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Flask',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Code Generators',
      ],
      keywords='flask flask_now flask-now app-generator flask-app-generator app generator',
      url='http://github.com/ozanonurtek/flask-now',
      author='Ozan Onur Tek',
      author_email='ozanonurtek@gmail.com',
      install_requires=[
          'flask'
      ],
      packages=['flask_now'],
      include_package_data=True,
      zip_safe=False)

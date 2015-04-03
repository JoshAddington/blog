from setuptools import setup
import os


setup(name='djangoblog',
      version='0.1',
      description='Django Blog',
      author='Josh Addington',
      author_email='addington.code@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=[
           'Django>=1.7',
           'djangorestframework',
           'psycopg2',
           'requests',
           'whitenoise'],
      )

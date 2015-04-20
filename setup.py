from setuptools import setup
import os


setup(name='djangoblog',
      version='0.6',
      description='Django Blog',
      author='Josh Addington',
      author_email='addington.code@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=[
           'Django>=1.7',
           'djangorestframework',
           'django-grappelli',
           'psycopg2',
           'requests',
           'six',
           'whitenoise'],
      )

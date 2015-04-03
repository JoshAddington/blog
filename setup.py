from setuptools import setup
import os

required_packages = [
    'Django>=1.7'
]

setup(name='django',
      version='0.1',
      description='Django Blog',
      author='Josh Addington',
      author_email='addington.code@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=required_packages,
)

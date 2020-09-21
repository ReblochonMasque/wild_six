from setuptools import setup
import pip
import os
import sys

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]

setup(name='wild_six',
      version='0.1.1',
      description='A package that provides ...',
      url='https://andreacortis@bitbucket.org/andreacortis/versioned_dictionary.git',
      author='Andrea Cortis',
      author_email='andrea.cortis@gmail.com',
      license='MIT',
      packages=['wild_six'],
      include_package_data=True,
      zip_safe=False,
      install_requires=load_requirements("requirements.txt")
      )

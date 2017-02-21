from setuptools import find_packages, setup


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='pig_latin_microservice',
      version='1.0',
      description='Vicarious Pig Latin Microservice Project',
      author='Christopher Tham',
      platforms=['any'],
      license='MIT',
      packages=find_packages(),
      install_requires=required)
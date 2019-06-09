from setuptools import setup

setup(name='tenseFinder',
      version='0.1',
      description='simple English tense finder',
      url='https://github.com/AliKhalili/tensfinder',
      author='Ali Khalili',
      author_email='akyegane[at]gmail.com',
      license='MIT',
      packages=['TenseFinder'],
      install_requires=[
          'spacy',
      ],
      zip_safe=False)

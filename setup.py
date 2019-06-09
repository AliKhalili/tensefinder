from setuptools import setup

setup(name='tensFinder',
      version='0.1',
      description='simple English tens finder',
      url='http://github.com/storborg/funniest',
      author='Ali Khalili',
      author_email='akyegane[at]gmail.com',
      license='MIT',
      packages=['TensFinder'],
      install_requires=[
          'spacy',
      ],
      zip_safe=False)

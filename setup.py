from setuptools import setup


setup (name = 'stex',
       version = '1.0',
       packages = ['stex'],
       entry_points = {
           'console_scripts' : [
               'stex = stex.cli:main'
               ]
               })


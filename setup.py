from setuptools import setup

# name is the name of the package
# version is the version of the package
# packages is the list of packages that are included in the package
# author is the author of the package(Optional)
# author_email is the email of the author(Optional)
# url is the source code github(Optional)
# classifiers is  for the package for searching the package in PyPI (Optional)
# keywords is description of the package(Optional)
# install_requires is the list of dependencies of the package
# python_requires is the python version required for the package
setup (name = 'stex',
       version = '1.0',
       packages = ['stex', 'stexsecond'],
       author="nk7260ynpa",
       author_email="nk7260ynpa@gmail.com",
       url="https://github.com/nk7260ynpa/Package_example",
       classifiers=["Programming Language :: Python :: 3.5",
                    "Programming Language :: Python :: 3.6",
                    "Programming Language :: Python :: 3.7",
                    "Programming Language :: Python :: 3.8"],
       keywords="Description of the package",
       install_requires=['numpy', 'pandas'],
       python_requires='>=3.5')


# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()

def read_license():
    with open('LICENSE') as f:
        return f.read()

app_name = "mpl4qt"
app_description = 'Matplotlib widget for PyQt'
app_long_description = readme() + '\n\n'
app_platform = ["Linux"]
app_author = "Tong Zhang"
app_author_email = "zhangt@frib.msu.edu"
app_license = read_license()
app_url = "https://archman.github.io/mpl4qt/"
app_keywords = "widgets Qt designer PyQt matplotlib"
installrequires = [
    'matplotlib',
    #'PyQt5',
]

setup(
    name=app_name,
    version="2.2.0",
    description=app_description,
    long_description=app_long_description,
    author=app_author,
    author_email=app_author_email,
    url=app_url,
    platforms=app_platform,
    license=app_license,
    keywords=app_keywords,
    packages=find_packages(),
    entry_points={
        'gui_scripts': [
            'run_designer=mpl4qt.launchers.designer:main',
        ],
        'console_scripts': [
            'mplcurve_default_settings=mpl4qt.widgets.utils:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules', 
    ],
    install_requires=installrequires,
)

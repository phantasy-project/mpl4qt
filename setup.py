# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()

app_name = "mpl4qt"
app_description = "Data visualization widgets for PyQt5"
app_long_description = readme() + '\n\n'
app_platform = ["Linux"]
app_author = "Tong Zhang"
app_author_email = "zhangt@frib.msu.edu"
app_url = "https://phantasy-project.github.io/mpl4qt/"
app_keywords = "widgets Qt designer PyQt matplotlib"
installrequires = [
    'matplotlib',
    'PyQt5',
    'pandas',
    'openpyxl', # save data as xlsx
    'tables', # save data as hdf5
    'tzlocal',
]
extras_require = {
    'dev': ['pyqt5-tools'],
}

setup(
    name=app_name,
    version="2.8.3-1",
    description=app_description,
    long_description=app_long_description,
    long_description_content_type='text/markdown',
    author=app_author,
    author_email=app_author_email,
    url=app_url,
    platforms=app_platform,
    license='MIT',
    keywords=app_keywords,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'gui_scripts': [
            'run_designer=mpl4qt.launchers.designer:main',
        ],
        'console_scripts': [
            'mplcurve_default_settings=mpl4qt.widgets.utils:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    install_requires=installrequires,
    extras_require=extras_require,
)

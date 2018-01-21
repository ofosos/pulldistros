"""A setuptools config for pulldistros
"""

# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='pulldistros',  # Required

    version='0.1',  # Required

    description='Scrape distrowatch.com',  # Required

    url='https://github.com/ofosos/pulldistros',  # Optional

    author='Mark Meyer',  # Optional

    author_email='mark@ofosos.org',  # Optional

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='scape web distrowatch',  # Optional

    py_modules=['pulldistros'],

    install_requires=['bs4', 'requests', 'html5lib']

)

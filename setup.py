#!/usr/bin/env/python
from setuptools import setup

setup(
    name='ckanext-aerdbtheme',
    version='0.1',
    description='',
    license='AGPL3',
    author='',
    author_email='',
    url='',
    namespace_packages=['ckanext'],
    packages=['ckanext.aerdbtheme'],
    zip_safe=False,
    entry_points = """
        [ckan.plugins]
        aerdb_theme = ckanext.aerdbtheme.plugins:CustomTheme
    """
)

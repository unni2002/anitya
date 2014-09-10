#!/usr/bin/env python

"""
Setup script
"""

# Required to build on EL6
__requires__ = ['SQLAlchemy >= 0.7', 'jinja2 >= 2.4']
import pkg_resources

from setuptools import setup
from anitya.app import __version__


setup(
    name='anitya',
    description='anitya is a project to monitor upstream releases in a distro.',
    version=__version__,
    author='Pierre-Yves Chibon',
    author_email='pingou@pingoured.fr',
    maintainer='Pierre-Yves Chibon',
    maintainer_email='pingou@pingoured.fr',
    license='GPLv2+',
    download_url='https://fedorahosted.org/releases/a/n/anitya/',
    url='https://fedorahosted.org/anitya/',
    packages=['anitya'],
    include_package_data=True,
    scripts=['files/anitya_cron.py'],
    install_requires=[
        'Flask', 'SQLAlchemy>=0.6', 'wtforms', 'flask-wtf',
        'python-fedora', 'python-openid', 'straight.plugin',
        'python-dateutil', 'bunch', 'markupsafe', 'fedmsg'
    ],
)

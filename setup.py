
"""

Author: Nikola Vukovic | @vukovicnikola | www.nikola.me |
Description: Script to initialise a directory structure for new projects
Last Updated: Wed Nov 22 2017

"""

#!/usr/bin/env python3

from setuptools import setup

setup(name='templateproject',
      version='0.1',
      description='Generate Template Directory Structure for Projects',
      url='http://github.com/vukovicnikola/templateproject',
      author='Nikola Vukovic',
      author_email='contact@nikola.me',
      license='MIT',
      packages=['templateproject'],
      entry_points = {
        'console_scripts': ['init_proj=templateproject.command_line:main'],
        },
      include_package_data=True,
      zip_safe=False)

"""

Author: Nikola Vukovic | @vukovicnikola | www.nikola.me |
Description: Script to initialise a directory structure for new projects
Last Updated: Wed Nov 22 2017

"""

#!/usr/bin/env python3

import os
from datetime import datetime

###################### SPECIFY DIRECTORY STRUCTURE ###########################

__root_dirs = {
                '1_admin': {'1_proposals': None,
                            '2_finance': None,
                            '3_reports': None},
                '2_ethics': {'1_approval': None,
                             '2_consent': None},
                '3_experiment': {'1_collection': None,
                                 '2_data': {'1_raw': None,
                                            '2_interim': None,
                                            '3_processed': None},
                                 '3_analysis': {'funcs': None,
                                                'models': None,
                                                'notebooks': None},
                                 '4_outputs': {'1_figures': None,
                                              '2_reports': None}
                                },
                '4_dissemination': {'1_presentations': None,
                                    '2_publications': None,
                                    '3_publicity': None}
                # add more root directories here if needed
                }

###################### CREATE DIRECTORY STRUCTURE ############################
def init_proj(project_name):
    cw_dir = os.getcwd() # get current directory
    project_path = os.path.join(cw_dir,project_name)
    if not os.path.isdir(project_path):
        os.mkdir(project_path)
        __mkdirs_from_dict(project_path)
        __mk_boiler_files(project_path)
    else:
        raise OSError('Specified project directory already exists!')

def __mkdirs_from_dict(project_path, dirdict=__root_dirs):

    # create root project hierarchy
    for key, val in dirdict.items():
        os.mkdir(os.path.join(project_path, key))
        # create subfolders if specified
        if type(val) == dict:
            __mkdirs_from_dict(os.path.join(project_path, key), dirdict=val)


###################### CREATE BOILERPLATE FILES ##############################

def __mk_boiler_files(project_path):
    # __init__.py
    init_path = os.path.join(project_path,'3_experiment/3_analysis/funcs/__init__.py')
    open(init_path, 'a').close()

    # LICENSE.txt
    license_path = os.path.join(project_path,'3_experiment/3_analysis/LICENSE.txt')
    license_file = open(license_path, 'a')
    license_file.writelines(
["MIT License\
\n\n\
Copyright (c) ", str(datetime.now().year), " {{ Author }}\
\n\n\
Permission is hereby granted, free of charge, to any person obtaining a copy of\
 this software and associated documentation files (the \"Software\"), to deal \
in the Software without restriction, including without limitation the rights \
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell \
copies of the Software, and to permit persons to whom the Software is \
furnished to do so, subject to the following conditions:\
\n\n\
The above copyright notice and this permission notice shall be included in all\
 copies or substantial portions of the Software.\
\n\n\
THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR \
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, \
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE \
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER \
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, \
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE \
SOFTWARE."])
    license_file.close()

    # README.md
    readme_path = os.path.join(project_path,'3_experiment/3_analysis/README.md')
    readme_file = open(readme_path, 'a')
    readme_file.writelines(
    ["# Sample Project README\n\
> A short description of what the project is about\n\
----------------\n\
Longer project description...\n\n\
## Requirements\n\
----------------\n\
- [Requirement 1](https://www.google.com)\n\n\
## Installation\n\
----------------\n\
Install the package in terminal using:\n\
```sh\n\
pip install 'package'\n\
```\n\n\
## Usage\n\
----------------\n\
Describe how to use the project...\n\n\
## Author\n\
----------------\n\
@Author – [https://github.com/username/](https://github.com/username/)\n\n\
Distributed under the MIT license. See LICENSE.txt for more information."]
    )
    readme_file.close()

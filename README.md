# Directory Structure for Science Projects
> A simple python package to generate a logical, standardised, and flexible directory hierarchy for academic research
----------------

Science projects tend to generate a lot of documents, ranging from project proposals, ethics forms, notes and to-do lists, publication drafts, graphs, PowerPoint presentations – to name just a few. Not to mention all the experimental materials, data, and analysis code. It's easy to see how managing these can quickly become stressful and challenging. Indeed, in the past I've authored quite a number of poorly managed project folders myself. Some of them grew to such proportions they ended up developing sentience and serious self-esteem issues.

Happily, I've developed an approach to manage the digital side of my research more successfully and automatically - and so can you! The key is in adopting a logical and consistent project folder structure. Having this before you start a research project means you can work efficiently, find files more easily, prevent duplication, and be able to share and collaborate while minimising the risk of data loss.

![](img/init_proj.gif)

## Requirements
----------------
- [Python 2.7 or 3.5](https://www.python.org/downloads/)

## Installation
----------------
Install the package in terminal using pip:
```sh
pip install templateproject
```
or install directly from GitHub, so that source changes will be immediately available after updates:
```sh
pip install git+https://github.com/vukovicnikola/templateproject.git
```
## Usage
----------------
After installing the package, you can use the terminal to initialise a new project structure:
```sh
init_proj your-project-name
```


## Project Folder Structure
----------------
```
./your-project-name/
├── 1_admin
│   ├── 1_proposals         <-- project background, plans, proposals and applications...
│   ├── 2_finance           <-- funding applications, receipts, project budgets...
│   └── 3_reports
├── 2_ethics
│   ├── 1_approval          <-- ethics application, approval docs...
│   └── 2_consent           <-- consent forms, questionnaires...
├── 3_experiment
│   ├── 1_collection        <-- data collection scripts, experimental stimuli and code...
│   ├── 2_data
│   │   ├── 1_raw           <-- original (read only) data files, e.g. raw reaction time data, etc...
│   │   ├── 2_interim       <-- intermediary files, pre-processed or transformed data...
│   │   └── 3_processed     <-- final canonical datasets for modeling and stats...
│   ├── 3_analysis(*)
│   │   ├── funcs           <-- source functions for processing, modeling, visualisation....
│   │   ├── models          <-- trained models, model predictions, coefficients...
│   │   └── notebooks       <-- Jupyter notebooks for data exploration, plotting...
│   └── 4_outputs
│       ├── 1_figures       <-- generated figures and graphics for reporting...
│       └── 2_reports       <-- project reports, HTML, PDF...
└── 4_dissemination
    ├── 1_presentations     <-- Keynote/PowerPoint slides, conference posters...
    ├── 2_publications      <-- journal articles, published conference proceedings...
    └── 3_publicity         <-- media coverage and publicity, newspaper articles, outreach...

* to facilitate version control of scripts in the analysis directory,
boilerplate files are added: an MIT LICENSE.txt, a README.md,
and a __init__.py to make the funcs directory act as a Python module.
```


## Author
----------------
Nikola Vukovic – [@vukovicnikola](https://twitter.com/vukovicnikola) – [www.nikola.me](http://www.nikola.me)

Distributed under the MIT license. See ``LICENSE.txt`` for more information.

[https://github.com/vukovicnikola/](https://github.com/vukovicnikola/)

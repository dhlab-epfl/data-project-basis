# Data Project Basis

This repo is intended as a sound basis for a python data project.
The goals are:
- reproducible data-science! structuring the project in readable steps, so that anyone can re-run your project easily.
- clear structure! 1 folder for your data, 1 for your scripts that do most of the work, 1 for your report, 1 for the reusable code that you use across multiple scripts (and even project).

An example of a real project using this structure is [dhs-nerd](https://github.com/dddpt-epfl-phd/dhs-nerd/).

## Folder structure

Folders:
- `scripts/`: this is where you'll spend most of your time, writing scripts to download data, train models, create graphs etc. Each main step of the project has its own numbered subfolder, for example:
    + `s0_download_data/`: with **numbered scripts** doing substeps such as `s0_download_data.py`, `s1_stats.ipynb` etc...
    + `s1_train_model/` ...
    + `s2_.../`
    + `data_filepaths.py`: when you output data files or figures images, their path is defined here as relative to main step folder (all paths begin with `../../XX/`), see [example file](https://github.com/dhlab-epfl/data-project-basis/blob/main/scripts/data_filepaths.py).
    + some configuration parameters that are reused across steps of the project? create some other file here! e.g. `config.py`, `plot_styles.py`, whatever you need
- `data/`: all the data you're outputting, the model parameters you obtain, etc, go in this folder, with numbered subfolders for each project step, following the previous example you would have: `s0_downloaded_data/`, `s1_models/`, `s3_...`. Note that this folder is ignored by git.
- `src/`: if you want to reuse some code across script, it goes here! e.g. if you have a `utils.py` file, that's his home ;-)
- `report/`: If you write your report in the repo, that's the place. If you save figures they go in:
    + `figures/`

In an ideal project, one should be able to run the **numbered scripts** one after the other and obtain the results you obtained.
Note that you can have unnumbered scripts for exploring/hacking around.

## Workflow

Usually, the workflow of the project goes like this:
1) explore/hack a subproblem with a simple ugly script, don't care about the project structure too much at this stage
2) it's ugly but it works: push it to git.
3) structure it cleanly as a numbered script:
    - clear variable names ;
    - add some comments for documentation ;
    - output data/figures in the proper places.
4) push to git
5) repeat from step 1) with your next subproblem
6) at some point, you'll find some pieces of code/functions you reuse often, add them to your `src/utils.py` file (or another file in `src/`)

## Python imports

To be able to import seamlessly python scripts/function from your `src/` `scripts/sX_XX` folders:
- each folder in `src/` and `scripts/` should have a `__init__.py` file, it's okay if it's empty
- each `.py`, `.ipynb` file should have the following lines before any imports of your local scripts:
```python
import sys 
sys.path.append("../../src")
sys.path.append("../../scripts")
```
After that you can import your functions from `src/utils.py` in `scripts/s0_(EXAMPLE)_download_data/s0_download_data.py` easily:
```
from utils import useful_function 
```
See example [`scripts/s0_(EXAMPLE)_download_data/s0_download_data.py`](https://github.com/dhlab-epfl/data-project-basis/blob/main/scripts/s0_(EXAMPLE)_download_data/s0_download_data.py) importing and using a function from [`src/utils.py`](https://github.com/dhlab-epfl/data-project-basis/blob/main/src/utils.py) for how it works.


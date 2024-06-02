## Install pyenv-win
https://github.com/pyenv-win/pyenv-win

## Setup environment
### Install python 3.10.1
> pyenv install 3.10.1
 
### Local python version in repo path
> pyenv local 3.10.1
 
### Poetry installation
> pyenv exec pip install poetry

### Activate environment
> poetry shell

### Install dependencies
> poetry install

## Django essentials
### Running
> python manage.py runserver

or
> manage.py runserver

### Make sure assets
> python manage.py collectstatic
 
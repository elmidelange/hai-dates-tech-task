# Harrison AI Dates Tech Task
> This module computes the number of days between two dates.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## General Information
The aim of the project is to compute the difference between two dates from scratch. I.e. without importing or otherwise building on existing packages for date processing.
Timezones were not considered and the dates were expected to be of format `YYYY-MM-DD` and based of the [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar).


## Technologies Used
- [Poetry](https://python-poetry.org/) - Python package and dependency management
- [Docker](https://www.docker.com/) - Containerisation tool
- [VSCode Remote Containers](https://code.visualstudio.com/docs/remote/containers) - Containerised development
- [GitHub Actions](https://github.com/features/actions) - CI/CD tool


## Features
- Python module to calculate date difference (`dates/date_diff.py`) with tests (`dates/tests/`)
- Dockerfile for reproducibility across dev and future 'prod' environments
- CI/CD pipeline (`.github/workflows/`) for automated testing & PyPI packaging


## Setup
1. System Dependencies
    - [Python^3.8][https://www.python.org/downloads/]
    - [Poetry](https://python-poetry.org/)
2. Install dependencies
    - `poetry install`
3. Activate poetry virtual environemnt
    - `poetry shell`


## Usage

### CLI Usage

```bash
python main.py --date1 "2012-01-10" --date2 "2012-01-11"
0
```

```bash
python main.py --date1 "2021-12-01" --date2 "2017-12-14"
1447
```

```bash
python main.py --date1 "20000-01-01" --date2 "2017-12-14"
ValueError: Year value must be of format YYYY for input 20000-01-01
```

```bash
python main.py --date1 "2022-02-29" --date2 "2017-12-14"
ValueError: YYYY-02-29 is only valid on a leap year for input 2022-02-29
```

### Docker Usage
```bash
docker build -t hai-dates .
docker run hai-dates --date1 "2012-01-10" --date2 "2012-01-11"
0
```

### Developer Usage
- Future features can be implemented by developing on a new branch (e.g. `dev`) and using the [Commitizen](https://commitizen-tools.github.io/commitizen/) tool to standardise commit messages.
- The `pre-commit-config.yaml` will run some basic code quality checks before commiting to GitHub.
- Tests and coverage can be run with `pytest --cov=dates`
- A push to the `main` branch will run the GitHub Actions CI/CD pipeline where it will run the following jobs:
1. Quality - linting & run rests
2. Release - peforms [semantic versioning](https://python-semantic-release.readthedocs.io/en/latest/) on the repository by updating the version and applying it both the `pyproject.toml` file and a new Git tag version.
3. Publish - publishes a new package version to TestPyPI
- A push to main that doesn't contain `fix`, `feat` or `BREAKING CHANGE` in the commit message will only run the `Quality` job in the CI/CD pipeline. If these key words are present it will create a new release version (major=`BREAKING CHANGE`, minor=`feat`, patch=`fix`) and publish it to PyPI.

### Test PyPI
``bash
python3.8 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ dates
```


## Room for Improvement
- Allow the module to accept different date formats (e.g. 'DD-MM-YYYY')
- Add code test coverage requirement to CI/CD pipeline
- Add docker container build & push step in CI/CD pipeline
- Developer documentation ( e.g. [Sphynx](https://www.sphinx-doc.org/en/master/))

## Acknowledgements
- Thanks Danny for setting this up! And Andy, Leo & Hong for reviewing :)


## Contact
Created by [@elmidelange](https://github.com/elmidelange) - feel free to contact me!

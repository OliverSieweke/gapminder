<!--suppress HtmlDeprecatedAttribute | JetBrains Inspection -->

<p align="center">
    <a href="https://choosealicense.com/licenses/mit">
      <img alt="License: MIT" src="https://img.shields.io/github/license/OliverSieweke/gapminder"/>
    </a>
    <a href="https://github.com/OliverSieweke/gapminder/graphs/traffic">
      <img alt="Downloads" src="https://img.shields.io/github/downloads/OliverSieweke/gapminder/total"/>
    </a>
    <a href="https://mybinder.org/v2/gh/OliverSieweke/gapminder/master?filepath=notebooks%2Fexploration.ipynb">
        <img alt="Binder" src="https://mybinder.org/badge_logo.svg" />
    </a>
</p>

<h1 align="center">
    gapminder
</h1>

Welcome to gapminder!


- [User Guide](#user-guide)
- [Data](#data)
- [Developer Guide](#developer-guide)

---

## User Guide

### Viewing the Project



### Running the Project

#### Locally

If you have [Python 3](https://www.python.org/downloads/) and [Jupyter](https://jupyter.org/install) installed, you may run the project on your local machine by executing the following commands from your terminal:

```bash
$ git clone https://github.com/OliverSieweke/gapminder.git
$ cd gapminder
$ pip install -r requirements.txt
$ jupyter notebook notebooks
```

---

## Data

The data used for this project was downloaded from [gapminder.org](https://www.gapminder.org/data/) on the 23.04.2020, it makes use of:

- [Total Population](https://www.gapminder.org/data/documentation/gd003/)

- [Life expectancy at birth](https://www.gapminder.org/data/documentation/gd004/)

- [Babies per woman (total fertility rate)](https://www.gapminder.org/data/documentation/gd008/)

  

------

<!--suppress HtmlDeprecatedAttribute | JetBrains Inspection -->
<p align="center">
    <a>
      <img alt="Python 3.7" src="https://img.shields.io/badge/python-3.7-blue.svg"/>
    </a>
    <a href="https://github.com/psf/black">
      <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"/>
    </a>
    <a href="https://dependabot.com/">
        <img alt="Dependabot" src="https://badgen.net/dependabot/OliverSieweke/gapminder/?icon=dependabot"/>
    </a>
    <a href="https://github.com/OliverSieweke/gapminder/releases">
        <img alt="Version" src="https://img.shields.io/github/v/tag/OliverSieweke/gapminder"/>
    </a>
</p>

## Developer Guide

Contributions are welcome! Please fork the project, make sure you have [Python 3.7](https://www.python.org/downloads/) installed and set up your local repository as follows: :

```bash
$ git clone https://github.com/<path_to_your_fork>
$ cd <your_local_repository>
$ python3.7 -m pip install -r requirements-dev.txt
$ pre-commit install
```

This will install required dependencies and set up git hooks to ensure that your commits conform to the project's code style.




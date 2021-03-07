# networkmedia
[![build status](https://github.com/avisionh/networkmedia/workflows/black/badge.svg)](https://github.com/avisionh/networkmedia/actions) [![Coverage Status](https://coveralls.io/repos/github/avisionh/networkmedia/badge.svg?branch=main)](https://coveralls.io/github/avisionh/networkmedia?branch=main) [![CodeFactor](https://www.codefactor.io/repository/github/avisionh/networkmedia/badge)](https://www.codefactor.io/repository/github/avisionh/networkmedia) [![License: MIT](https://img.shields.io/badge/License-MIT-informational.svg)](https://opensource.org/licenses/MIT) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Overview
Proof-of-concept for linking media content to create a network joining people of similar interests together.

## Requirements
To run the code in here, ensure your system meets the following requirements:
- Unix-like operating system (macOS, Linux, ...);
- [`direnv`](https://direnv.net/) installed, including shell hooks;
- [`.envrc`](https://github.com/alphagov/govuk-entity-personalisation/blob/main/.envrc) allowed/trusted by `direnv` to
  use the environment variables - see [below](#allowingtrusting-envrc);
- Python 3.8 or above; and
- [Poetry](https://python-poetry.org/docs/) installed.

Note there may be some Python IDE-specific requirements around loading environment variables, which are not considered here.

### 0. tl;dr
For quickstart set-up of the project, run the below in your shell:
```shell script
# 1. read project-specific environment variables
direnv allow

# 2. activate virtual environment and install package dependencies
poetry shell
poetry install

# 3. check adherence to good standards via pre-commit hooks
pre-commit install
```

### 1. Allowing/trusting `.envrc`

To read project-specific environment variables, allow/trust the [`.envrc`](.envrc) run the below in your shell at the top-level of this directory (where this `README.md` is located).

```shell script
direnv allow
```

> **Note:** If you are using PyCharm, then you will need to apply a few more steps before running `direnv allow` in your shell:
> 1. In your shell, run `poetry add python-dotenv`.
> 1. On PyCharm, click `PyCharm` -> `Preferences` -> `Plugins` and download the `EnvFile` plugin.
> 1. On PyCharm, edit your configuration to `Enable EnvFile` by ticking the checkbox.
> 1. On PyCharm, click `PyCharm` -> `Preferences` -> `Build, Execution, Deployment` -> `Console` -> `Python Console` and in the `Starting script` section, add the following Python code:
>    + `from dotenv import load_dotenv`
>    + `load_dotenv()`

### 2. Initialising the project environment
This repository uses [Poetry](https://python-poetry.org/docs/) to manage virtual environments and package dependencies. To set this up so you are working within the same Python version and with the same package versions, run the following in your shell:

```shell script
# activate virtual environment
poetry shell

# install dependencies in poetry.lock
poetry install
```

More information can be found on the [Poetry docs](https://python-poetry.org/docs/basic-usage/).

> **Note:** If you are using PyCharm, then you will need to apply a few more steps to use this Poetry environment:
> 1. On PyCharm, click `PyCharm` -> `Preferences` -> `Plugins` and download the [`Poetry`](https://plugins.jetbrains.com/plugin/14307-poetry) by @koxudaxi plugin.
> 1. On PyCharm, add the existing Poetry environment to the project.

#### Adding new packages
When adding new packages using Poetry, run the following in your shell:
```shell script
poetry add <package_name>
```
This should then update your `poetry.lock` file with the new package installed. Ensure this change is also version-controlled.

### 3. Installing pre-commit hooks
This repo is configured so `pre-commit` is run automatically on *every commit*. By running on each commit, we ensure that `pre-commit` will be able to detect all contraventions and keep our repo in a healthy state.

In order for `pre-commit` to run, configure it on your system by running the following in your shell.
```shell script
pre-commit install
```

#### If `pre-commit` detects secrets during commit:

If `pre-commit` detects any secrets when you try to create a commit, it will detail what it found and where to go to check the secret.

If the detected secret is a false-positive, you should update the secrets baseline through the following steps:

- Run `detect-secrets scan --update .secrets.baseline` to index the false-positive(s);
- Next, audit all indexed secrets via `detect-secrets audit .secrets.baseline` (the same as during initial set-up, if a
secrets baseline doesn't exist); and
- Finally, ensure that you commit the updated secrets baseline in the same commit as the false-positive(s) it has been
updated for.

If the detected secret is actually a secret (or other sensitive information), remove the secret and re-commit. There is no need to update the secrets baseline in this case.

If your commit contains a mixture of false-positives and actual secrets, remove the actual secrets first before updating and auditing the secrets baseline.

#### Note on Jupyter notebook cleaning

It may be necessary or useful to keep certain output cells of a Jupyter notebook, for example charts or graphs visualising some set of data. To do this, add the following comment at the top of the input block:

```shell script
# [keep_output]
```

This will tell `pre-commit` not to strip the resulting output of this cell, allowing it to be committed.

### 4. Managing secrets
To hold secrets like API credentials without exposing them in the repo, create a `.secrets` file like [this example](https://gist.github.com/avisionh/f8c9b31c02440db041442fa54e9adea3). This should be automatically read by the `.envrc` file.

For instance, if you want to download data onto your system directly through the Kaggle API, you will need credentials to connect to the Kaggle API. To do this, go the Account Tab (https://www.kaggle.com/<username>/account) and click *‘Create API Token’*. This will download a `kaggle.json` file. Copy and paste the entries into your `.secrets` file, by populating it with the following:
```shell script
export KAGGLE_USERNAME="<your_user_name>"
export KAGGLE_KEY="<your_api_key>"
```

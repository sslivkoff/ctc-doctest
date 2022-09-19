# Installation


## Basic Installation

Installing `ctc` takes 2 steps:
1. `pip install checkthechain`
2. `ctc setup` in the terminal to run the setup wizard (can skip most steps by pressing enter)

See [Configuration](configuration) for additional setup options.

If your shell's `PATH` does not include python package scripts, you need to do something like `python3 -m pip ...` and `python3 -m ctc ...`

Installation requires python 3.7 or greater. see [Dependencies](dependencies) for more information.


## Upgrading

Upgrading to a new version of `ctc` takes two steps:
1. `pip install checkthechain -U`
2. Rerun the setup wizard by running `ctc setup` (can skip most steps by pressing enter)

To upgrade from a special installation, you may need to 


## Uninstalling

Fully removing `ctc` from a machine takes three steps:
1. Uninstall the package `pip uninstall checkthechain`
2. Remove the config folder: `rm -rf ~/.config/ctc`
3. Remove the data folder: `rm -rf ~/ctc_data`

You can always check whether a package has been uninstalled from your python environment by attempting to import it in a fresh shell. If you see a `ModuleNotFoundError`, the package has been uninstalled.

```python
>>> import ctc
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'ctc'
>>> # ctc is not uninstalled
```

## Special Installations

### Installing from source

If you would like to install the latest version of `ctc` you can clone the repo directly:

```bash
git clone 
cd checkthechain
python -m pip install ./
```

### Installing in develop mode / edit mode

If you would like to make edits to the `ctc` codebase and actively use those edits in your python programs, you can install the package in developer mode with the `-e` flag:

```bash
git clone 
cd checkthechain
python -m pip install -e ./
```


## Libraries

On a fresh installation of Ubuntu or Debian, you may need to manually install the `build-essential` and `python-dev` packages. Machines that are used for active python development probably already have these packages installed.

```bash
PYTHON_VERSION=$(python3 -c "import sys; print('python' + str(sys.version_info.major) + '.' + str(sys.version_info.minor))")

python3 -m pip install $PYTHON_VERSION-dev
sudo apt-get install build-essential
```

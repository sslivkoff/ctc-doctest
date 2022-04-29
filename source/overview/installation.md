# Installation


## Basic Installation

Installing `ctc` takes two steps:
1. `pip install checkthechain`
2. run `ctc setup` in terminal to run setup wizard (see [Configuration](/overview/configuration) details)

If your shell's `PATH` does not include python scripts you may need to do something like `python3 -m pip ...` and `python3 -m ctc ...`

Installation requires `python >= 3.7`


## Upgrading

Upgrading to a new version of `ctc` takes two steps:
1. `pip install checkthechain -U`
2. run `ctc setup` to add any new data to the data directory (can skip most steps by pressing enter)


## Alternative Installations

### Installing from source

If you would like to install the latest version of `ctc` you can clone the repo directly:

```bash
git clone 
cd checkthechain
python -m pip install ./
```

### Installing in Develop Mode / Edit Mode

If you would like to make edits to the `ctc` codebase and actively use those edits in your python programs, you can install the package in developer mode with the `-e` flag:

```bash
git clone 
cd checkthechain
python -m pip install -e ./
```


## Libraries

On a fresh installation of Ubuntu or Debian you may need to manually install the `build-essential` and `python-dev` packages:
```bash
PYTHON_VERSION=$(python3 -c "import sys; print('python' + str(sys.version_info.major) + '.' + str(sys.version_info.minor))")

python3 -m pip install $PYTHON_VERSION-dev
sudo apt-get install build-essential
```


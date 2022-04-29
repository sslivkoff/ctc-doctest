# Dependencies

```{admonition} TLDR
This page is only aimed at users that would like know what `ctc` depends on under the hood.

If you just want to install `ctc` then check out the [Installation](/overview/installation) docs.
```


## OS Dependencies

Usage of `ctc` requires `python >=3.7, <= 3.10`.

When using a fresh installation of Debian or Ubuntu, you may need to manually install `build-essential` and `python-dev`. These are libraries required by many python packages including ctc. If you are an active python user you likely already have these installed, as they are required for many standard packages. If you are setting up a new machine or environment, you may need to install them according to your operating system and python version:

```
To install on Debian / Ubuntu can use the following:

PYTHON_VERSION=$(python3 -c "import sys; print('python' + str(sys.version_info.major) + '.' + str(sys.version_info.minor))")

python3 -m pip install $PYTHON_VERSION-dev
sudo apt-get install build-essential
```

## Libraries

`ctc` depends on a few different types of external packages:

1. **data science dependencies** include standard python library packages including `numpy`, and `pandas`.
2. **IO dependencies** include data formatting
3. **toolsuite dependencies** are general python utilities coming the `toolsuite` set of repos. These are written by the same authors as `ctc`.
4. **EVM/Cryptography dependencies** include `pycryptodome`, `rlp`, and `eth_abi`.

Note also that each of these dependencies has its own dependencies.

Reliance on these packages will be minimized in future releases to minimize attack surface and to maximize the number of environments in which `ctc` can be run. Some of the common libraries in the EVM ecosystem have incompatible requirements. For example, `ethereum-etl` requires older versions of `web3py` and `eth_abi`, and so a single environment cannot contain the most recent versions of all of these packages. `ctc` aims to avoid these types of compatibility problems by minimizing dependencies.


## Type Checking

`ctc` uses python's type annotations for static analysis of the codebase. This helps catch errors before they can appear at runtime. Custom types used by `ctc` can be found in [the `ctc.spec` subpackage](https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/spec/typedefs).

Checks are currently performed using `mypy=0.930`. Future `mypy` versions and features will be used as they become available. End users of `ctc` do not need `mypy` unless they are interested in running these type checks.

New python type annotation features will be used as they become available using [`typing_extensions`](https://github.com/python/typing/tree/master/typing_extensions). By using `from __future__ import annotations`, most of these features can be used without compromising backward compatibility.


## Testing

`ctc` tests are run pytest 7.0.0 with the `pytest-asyncio` extension. These can be run using `pytest .` in [the `/tests` directory](https://github.com/fei-protocol/checkthechain/tree/main/tests).


## Documentation

`ctc` documentation is built using `sphinx` 4.5.0 using the readthedocs theme (`sphinx-rtd-theme`) and the `myst-parser` extension for parsing markdown.

[Source files](https://github.com/fei-protocol/checkthechain/tree/main/docs) for the docs can be found in the main repo.


## Databases

`ctc` stores much of the data it downloads in sql databases. Support for sqlite is already implemented and support for postgresql is on the way. 

For more details see [Data Storage](/data_ops/storing_data)


# Dependencies

```{admonition} TLDR
This page is only aimed at users that would like know what `ctc` depends on under the hood.

If you just want to install `ctc` then check out the [Installation](/overview/installation) docs.
```


## OS Dependencies

Usage of `ctc` requires `python >=3.7, <= 3.10`.

When using a fresh installation of Debian or Ubuntu, you may need to manually install `build-essential` and `python-dev`. These are libraries required by many python packages including `ctc`. If you are an active python user it's likely that you already have these installed. If you are setting up a new machine or environment, you may need to install them according to your operating system and python version:

To install on a fresh Debian / Ubuntu machine, can use the following:
```

PYTHON_VERSION=$(python3 -c "import sys; print('python' + str(sys.version_info.major) + '.' + str(sys.version_info.minor))")

python3 -m pip install $PYTHON_VERSION-dev
sudo apt-get install build-essential
```

## Libraries

`ctc` depends on a few different types of external packages:

1. **data science dependencies** include standard python library packages including `numpy`, and `pandas`.
2. **IO dependencies** include packages like `aiohttp` for network communication and `toml` for file io.
3. **toolsuite dependencies** are general python utilities coming the `toolsuite` set of repos. These are written by the same authors as `ctc`.
4. **EVM/Cryptography dependencies** include `pycryptodome`, `rlp`, and `eth_abi`.

Each of these dependencies has its own dependencies.

Reliance on these packages will be minimized in future releases to minimize attack surface and to maximize the number of environments in which `ctc` can be run. Some of the common libraries in the EVM ecosystem have incompatible requirements. For example, `ethereum-etl` requires older versions of `web3py` and `eth_abi`, and so a single environment cannot contain the most recent versions of all of these packages.


## Type Checking

`ctc` uses `mypy` for static analysis of type annotations. This helps catch errors before they can appear at runtime. Custom types used by `ctc` can be found in [the `ctc.spec` subpackage](https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/spec/typedefs).

Checks are currently performed using `mypy=0.930`. Future `mypy` versions and features will be used as they become available. End users of `ctc` do not need `mypy` unless they are interested in running these type checks.

New python type annotation features will be used as they become available using [`typing_extensions`](https://github.com/python/typing/tree/master/typing_extensions). By using `typing_extensions` and `from __future__ import annotations`, new typing features can be used as they are released without sacrificing backward compatibility.


## Testing

`ctc` tests are run using `pytest 7.0.0` with the `pytest-asyncio` extension. These can be run using `pytest .` in [the `/tests` directory](https://github.com/fei-protocol/checkthechain/tree/main/tests).


## Documentation

`ctc` documentation is built using `sphinx` 4.5.0. Source files and build instructions can be found in the [Documentation Repository](https://github.com/fei-protocol/checkthechain-docs).


## Databases

`ctc` stores much of the data it downloads in sql databases. Support for sqlite is currently in beta and support for postgresql is coming soon.

For more details see [Data Storage](/data_ops/storing_data)


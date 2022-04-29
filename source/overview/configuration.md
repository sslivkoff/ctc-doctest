
# Configuration

The behavior of `ctc` can be configured. This configuration is currently very simple and is mainly used to use specify custom RPC endpoints and data storage options.

```{admonition} TLDR
Run `ctc setup` on the command line to create the config. Run it again to edit the config
```

## Config Parameters

The `ctc` config consists of the following key-value pairs:
- **`config_spec_version`**: the `ctc` version used to create the config
- **`data_dir`**: the directory where `ctc` stores its data
- **`providers`**: metadata about rpc providers
- **`networks`**: metadata about custom networks including their names and chain_id's
- **`network_defaults`**: specification of the default provider to use for each network, and the default network

The main parameters of interest will usually be `providers` and `network defaults`.

An exact specification for the config can be found in [the config typedefs](https://github.com/fei-protocol/checkthechain/blob/main/src/ctc/spec/typedefs/config_types.py) file.

## Setting Config Parameters

By default ctc will looks for a config file at `~/.config/ctc/config.json`. But if the `CTC_CONFIG_PATH` environment variable is set, it will use that path instead.

Users do not need to directly create or edit `ctc` config files. Instead, all config parameters can be adjusted by using the setup wizard, activating by entering `ctc setup` on the command line. This can be used both for creating new configs and modifying the current config.

## Reading Config Parameters

On the command line, using `ctc config` will print information about the config, including its location on the filesystem and its current values.

In python, the `ctc.config` module has many functions for getting the current config path and its values:
```python
from ctc import config

config_path = config.get_config_path()
data_dir = config.get_data_dir()
providers = config.get_providers()
```

## Example Config

```python
{
    'config_spec_version': '0.2.10',
    'data_dir': '/home/storm/ctc_data',
    'networks': {},
    'providers': {
        'alchemy_mainnet': {
            'name': 'alchemy_mainnet',
            'network': 'mainnet',
            'protocol': 'http',
            'url': 'https://some-mainnet-rpc-url',
            'session_kwargs': {},
            'chunk_size': None,
        },
        'alchemy_arbitrum': {
            'name': 'alchemy_arbitrum',
            'network': 'arbitrum',
            'protocol': 'http',
            'url': 'https://some-mainnet-rpc-url',
            'session_kwargs': {},
            'chunk_size': None,
        },
    },
    'network_defaults': {
        'default_network': 'mainnet',
        'default_providers': {
            'mainnet': 'alchemy_mainnet',
            'arbitrum': 'alchemy_arbitrum',
        },
    },
    'db_configs': {
        'main': {'dbms': 'sqlite', 'path': '/home/storm/ctc_data/ctc.db'}
    },
}
```


TH

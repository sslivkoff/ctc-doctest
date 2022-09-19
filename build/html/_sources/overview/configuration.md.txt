
# Configuration

```{admonition} TLDR
Run `ctc setup` on the command line to create the config. Run it again to edit the config.
```

`ctc` uses a configuration file to control its behavior.

## Config Parameters

The config file consists of key-value pairs. The keys:
- **`config_spec_version`**: the `ctc` version used to create the config
- **`data_dir`**: the directory where `ctc` stores its data
- **`providers`**: metadata about RPC providers
- **`networks`**: metadata about networks including their names and `chain_id`'s
- **`default_network`**: default network to use
- **`default_providers`**: default provider for each network
- **`db_configs`**: database configuration information
- **`log_rpc_calls`**: whether to log rpc calls
- **`log_sql_queries`**: whether to log sql queries

A python type specification for the config can be found in [the config typedefs](https://github.com/fei-protocol/checkthechain/blob/main/src/ctc/spec/typedefs/config_types.py) file.

## Setting Config Parameters

By default ctc will looks for a config file at `~/.config/ctc/config.json`. But if the `CTC_CONFIG_PATH` environment variable is set, it will use that path instead.

Users do not need to directly create or edit `ctc` config files. Instead, all config parameters can be adjusted by using the setup wizard by running `ctc setup` on the command line. This can be used both for creating new configs and modifying the current config.

## Reading Config Parameters

On the command line, running `ctc config` will print information about the config including its location on the filesystem and its current values.

In python, the `ctc.config` module has many functions for getting config data:
```python
from ctc import config

config_path = config.get_config_path()
data_dir = config.get_data_dir()
providers = config.get_providers()
```

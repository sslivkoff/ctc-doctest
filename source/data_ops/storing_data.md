
# Storing Data

`ctc` places much of the data that it retreives into local storage.  This significantly improves the speed at which this data can be retrieved in the future. It also reduces the future load on those RPC nodes.

The model assumes that data is being queried from a remote RPC node. Some ultra performance-minded setups, such as running `ctc` on the same server as an archive node, might achieve better tradeoffs between speed and storage space by tweaking `ctc`'s local storage features.


## Data Storage Backends

`ctc` uses two main backends for storing data.

### Filesystem

`ctc` uses a data directory on the filesystem to store many types of chain data.

By default, `ctc` will place this folder in the user's home directory at `~/.ctc`. This is suitable for many setups. However, there are situations where it would be better to store data somewhere else, such as if the home directory is on a drive of limited size, or it the home directory is on a network drive with significant latency. The data directory can be moved by running the setup wizard `ctc setup`.


### SQL Databases

`ctc` also stores lots of data in SQL database tables. Schemas for these tables can be found [here](https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/db/db_spec/schemas). `ctc` currently supports sqlite with Postgresql support coming soon.

You can connect to the currently configured database by running `ctc db connect` in the terminal. Don't do this unless you know what you're doing.


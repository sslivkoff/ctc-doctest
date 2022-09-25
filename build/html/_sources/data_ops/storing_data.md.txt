
# Storing Data

`ctc` places much of the data that it retreives into local storage.  This significantly improves the speed at which this data can be retrieved in the future and it also reduces the future load on data sources.

The default configuration assumes that most data is being queried from a remote RPC node. Some performance-minded setups, such as running `ctc` on the same server as an archive node, might achieve better tradeoffs between speed and storage space by tweaking `ctc`'s local storage features.


## Data Storage Backends

`ctc` uses two main storage backends.

### Filesystem

`ctc` stores some files on the filesystem. By default, `ctc` will place its data folder in the user's home directory at `~/ctc_data`. This is suitable for many setups. However, there are situations where it would be better to store data somewhere else, such as if the home directory is on a drive of limited size, or it the home directory is on a network drive with significant latency. The data directory can be moved by running the setup wizard `ctc setup`.

Total storage usage of `ctc` on the filesystem can be found by checking the size of the `ctc` data directory.


### SQL Databases

`ctc` also stores lots of data in SQL database tables. Schemas for these tables can be found [here](https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/db/schemas). `ctc` currently supports sqlite with Postgresql support coming soon.

Total storage usage of `ctc` in the database can be found by running `ctc db -v` in the terminal.

You can connect to the currently configured database by running `ctc db login` in the terminal. Don't do this unless you know what you're doing.

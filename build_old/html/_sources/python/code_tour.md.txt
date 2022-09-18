
# Codebase Tour

## Architecture and API

- `ctc` does not use any custom types or OOP. Instead it emphasizes simple standard datatypes including python builtins, numpy arrays, and the occassional pandas dataframe. Effort is made to ensure that the users stay "close" to the data with minimal implicit magic going on.
- `ctc` is [asynchronous-first](async_code), which allows it to efficiently orchestrate large numbers of interdependent queries.
- `ctc` is designed with historical data in mind. Throughout its API many functions take parameters such as `block`, `blocks`, `start_block`, or `end_block` to specify the relevant block ranges for each query.


## Subpackages

There are a few subpackages that you should acquiant yourself with:

### ctc.evm

`ctc.evm` defines high-level functions for working with EVM data, and it contains most of the functions that users will need on a day-to-day basis. These are the "porcelain" functions, whereas the other `ctc` subpackages are the plumbing.

### ctc.protocols

`ctc.protocols` contains functions specific to many different protocols such as Chainlink or Uniswap.

### ctc.spec

`ctc.spec` is where most annotation types are defined.

### Other Subpackages

- `ctc.binary`: utilities for hashing and abi encoding/decoding
- `ctc.cli`: ctc command line implementation
- `ctc.config`: config loading and management
- `ctc.directory`: token and contract addresses as well as chain_id's 
- `ctc.rpc`: utilities for communicating over rpc
- `ctc.toolbox`: miscellaneous python utilities


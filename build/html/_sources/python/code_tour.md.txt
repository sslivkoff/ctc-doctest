
# Codebase Tour

There are a few subpackages that you should acquiant yourself with:

## ctc.spec

`ctc.spec` is where most datatypes are specified. These datatypes are used for type annotations throughout the codebase. ctc relies almost entirely on basic python types and functions rather than using OOP.


## ctc.evm

`ctc.evm` contains functions for working with EVM datatypes and it contains most of the functions that users will need on a day-to-day basis. These are the "porcelain" functions, whereas the other ctc subpackages are the plumbing.


## ctc.protocols

`ctc.protocols` contains functions specific to many different protocols such as Chainlink or Uniswap.


## Other Subpackages

- `ctc.binary`: utilities for hashing and abi encoding/decoding
- `ctc.cli`: ctc command line implementation
- `ctc.config`: config loading and management
- `ctc.directory`: token and contract addresses as well as chain_id's 
- `ctc.rpc`: utilities for communicating over rpc
- `ctc.toolbox`: miscellaneous python utilities


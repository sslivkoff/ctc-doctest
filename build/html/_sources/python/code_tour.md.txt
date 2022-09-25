
# Basic Usage

The top-level `ctc` module contains functions for generic EVM operations:

**Example: Generic EVM Operations**
```python
import ctc

some_hash = ctc.keccak_text('hello')

encoded_data = ctc.abi_encode_packed((400, 6000), '(int128,int128)')

eth_balance = await ctc.async_get_eth_balance('0x6b175474e89094c44da98b954eedeac495271d0f')

erc20_balance = await ctc.async_get_erc20_balance(
    token='0x6b175474e89094c44da98b954eedeac495271d0f',
    wallet='0x6b175474e89094c44da98b954eedeac495271d0f'],
    block=15000000,
)

events = await ctc.async_get_events(
    '0xcbcdf9626bc03e24f779434178a73a0b4bad62ed',
    event_name='Swap',
)
```

Some points to keep in mind while using `ctc`:
- `ctc` uses functional programming. Instead of custom types or OOP, `ctc` uses simple standard datatypes including python builtins and numpy arrays. There is no need to initialize any objects. Simply `import ctc` and then call functions in the `ctc.*` namespace.
- `ctc` is asynchronous-first, which allows it to efficiently orchestrate large numbers of interdependent queries. [Special consideration](async_code) is needed to run code in an asynchronous context.
- `ctc` is designed with historical data analysis in mind. For any query of EVM state, `ctc` aims to support historical versions of that query. Most `ctc` query functions take parameters that can specify a block or block range relevant to the query.

The top-level `ctc` package covers generic EVM operations, which are described in more detail [here](datatypes). There are also a few other `ctc` subpackages that are relevant to specific use-cases described below.

#### RPC Client Subpackage `ctc.rpc`

`ctc.rpc` implements `ctc`'s custom RPC client. This client can be used for fine-grained control over RPC calls. Unless explcitly told not to do so.`ctc` will automatically encode requests to binary and decode requests from binary.

**Example: get bytecode for contract, at specific block, using specific provider**
```python
import ctc.rpc

contract_bytecode = await ctc.rpc.async_eth_get_code(
    '0x6b175474e89094c44da98b954eedeac495271d0f',
    block_number=15000000,
    provider='https://some_rpc_node/',
)
```

### Protocol-specific Subpackages `ctc.protocols`

`ctc.protocols` contains functions specific to many different protocols such as Chainlink or Uniswap. See a full list [here](specific_protocols).

**Example: gather complete historical data for Chainlink's RAI-USD feed**
```python
from ctc.protocols import chainlink_utils

feed_data = await chainlink_utils.async_get_feed_data('RAI_USD')
```


### Other Subpackages

End users of `ctc` probably won't need to use any of these directly.

- `ctc.cli`: command line interface
- `ctc.config`: configuration utilities
- `ctc.db`: local cache database
- `ctc.spec`: ctc specifications, mainly types for type annotations
- `ctc.toolbox`: miscellaneous python utilities

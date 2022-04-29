
# Obtaining Data

`ctc` collects data from a variety of sources, including RPC nodes, metadata databases, block explorers, and crypto data aggregators. After initial collection, much of this data is then [stored](/data_ops/storing_data).

## Sources of Historical Data

`ctc` collects the majority of its data through RPC nodes using the EVM's [standard JSON-RPC interface](https://eth.wiki/json-rpc/API). Collection of historical data (as opposed to recent chain data) requires use of an archive node.

There are 3 main ways to gain access to an RPC node:

1. **Run your own node** Although this requires more time, effort, and hardware than the other methods, it often leads to the best results. [Erigon](https://github.com/ledgerwatch/erigon) is the most optimized client for running an archive node. 
2. **Use a 3rd-party private endpoint** Private RPC providers (e.g. [Alchemy](https://www.alchemy.com/), [Quicknode](https://www.quicknode.com/), or [Moralis](https://moralis.io/speedy-nodes/))
provide access to archive nodes, either through paid plans or sometimes even through free plans.
3. **Use a 3rd-party public endpoint** You can query data from public endpoints like Infura. This approach is not recommended for any significant data workloads, as it often suffers from rate-limiting and poor historical data availability.

`ctc`'s RPC config is created and modified by running the [setup wizard](/overview/configuration).


## Other types of data

Beyond RPC data there are a few other types of data that `ctc` collects, including:
- **ABIs of Contracts, Functions, and Events** from [Etherscan](https://etherscan.io/) and [4byte](https://www.4byte.directory/)
- **Market Data** from [CoinGecko](https://coingecko.com/)


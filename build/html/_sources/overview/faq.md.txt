# FAQ

## What are the goals of `ctc`?
- **Treat historical data as a first-class feature**: This means having historical data functionality well-integrated into each part of the of the API. It also means optimizing the codebase with historical data workloads in mind.
- **Clean API emphasizing UX**: With `ctc` most data queries can be obtained with a single function call. No need to instantiate objects. RPC inputs/outputs are automatically encoded/decoded by default.
- **Maximize data accessibility**: Blockchains contain vast amounts of data, but accessing this data can require large amounts of time, effort, and expertise. `ctc` aims to lower the barrier to entry on all fronts.

## Why use `async`?
`async` is a natural fit for efficiently querying large amounts of data from an archive node. All `ctc` functions that fetch external data use `async`. For tips on using `async` see [this section](/python/async_code) in the docs. Future versions of `ctc` will include some wrappers for synchronous code.

## Do I need an archive node?
If you want to query historical data, you will need an archive node. You can either [run one yourself](https://github.com/ledgerwatch/erigon) or use a third-party provider such as [Alchemy](https://www.alchemy.com/), [Quicknode](https://www.quicknode.com/) or [Moralis](https://moralis.io/speedy-nodes/). You can also use `ctc` to query current (non-historical) data using a non-archive node.

## Is `ctc` useful for recent, non-historical data?
Yes, `ctc` has lots of functionality for querying the current state of the chain.


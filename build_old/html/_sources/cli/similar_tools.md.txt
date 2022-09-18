
# Similar CLI tools

## ethereum-etl

[ethereum-etl](https://github.com/blockchain-etl/ethereum-etl) is a tool for collecting raw historical data from EVM chains, including blocks, transactions, erc20 transfers, and internal traces. Along with the rest of the [blockchain-etl stack](https://github.com/blockchain-etl), it powers the popular [BigQuery blockchain datasets](https://cloud.google.com/blog/products/data-analytics/introducing-six-new-cryptocurrencies-in-bigquery-public-datasets-and-how-to-analyze-them). The primary use case of `ethereum-etl` and its associated repos is to index a significant portion of a chain's history in preparation for large scale data analysis.

Prior to creating `ctc`, `ethereum-etl` was the primary data collection tool used by `ctc`'s authors. It was extensive use of `ethereum-etl` that inspired much of `ctc`'s design. Compared to `ethereum-etl`, `ctc` aims fall closer to the porcelain end of the [plumbing-vs-porcelain](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain) spectrum, with goals such as:
- create more diverse datasets, such as datasets that rely on `eth_call`
- create more targeted datasets, such as datasets focused on specific protocols like Chainlink or Uniswap
- create tighter integration with the python ecosystem
- go beyond data collection by creating a data analysis toolkit that serves each stage of the data analysis lifecycle
- implement quality-of-life improvements for the lazy
    - store and manage metadata such as addresses of tokens, oracles, and pools
    - automate tasks such as data encoding/decoding

## TrueBlocks

[TrueBlocks](https://github.com/TrueBlocks/trueblocks-core) is a tool for managing optimized local copies of EVM chain data. TrueBlocks then makes these local data copies accessible through an enhanced RPC interface. TrueBlocks excels at tracing and querying all appearances of a given address throughout a chain's history.

There's a decent amount of overlap between `ethereum-etl`, TrueBlocks, and `ctc`. Relatively speaking, `ethereum-etl` is plumbing, TrueBlocks is mostly plumbing with some porcelain, and `ctc` is mostly porcelain with some plumbing.

## ethereal, seth, and cast

[ethereal](https://github.com/wealdtech/ethereal) (go), [seth](https://github.com/dapphub/dapptools/tree/master/src/seth) ([dapptools](https://github.com/dapphub/dapptools), bash+javascript), and [cast](https://book.getfoundry.sh/reference/cast.html) ([foundry](https://github.com/gakonst/foundry), rust) are powerful command line utilities that each perform a wide range of EVM-related tasks.

`ctc` has lots of overlapping functionality with each. Where they differ is their focus. These other tools are more aimed at smart contract development, whereas `ctc` is more aimed at data collection and analysis. Compared to these tools, `ctc`'s biggest disadvantage is that it is limited to read-only operations. On the other hand `ctc`'s biggest advantage is its treatment of historical data as a first class feature.


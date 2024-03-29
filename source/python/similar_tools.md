
# Similar Python Tools

## web3.py

[web3.py](https://github.com/ethereum/web3.py) is a general purpose EVM library that is created and maintained by the Ethereum Foundation. Although web3.py and `ctc` have some overlapping functionality, they focus on different things. Web3.py supports full wallet functionality, whereas `ctc` is currently limited to read-only operations. Web3.py also supports a greater variety of communication protocols including websockets.

On the other hand, `ctc` is primarily aimed at historical data analysis. It contains more functions for aggregating historical datasets from various on-chain protocols. Additionally, web3.py is primarily synchronous, whereas `ctc` is primarily asynchronous.

## ape

[ape](https://github.com/ApeWorX/ape) is another general purpose EVM library that aims to improve upon web3.py in a variety of areas. Ape features direct integrations with many tools for both the development and deployment of smart contracts. Ape has plugins for many popular languages and tools including vyper, solidity, foundry, and hardhat.

## ethtx

[ethtx](https://github.com/ethtx/ethtx) is a library for decoding and summarizing individual transactions. You can see it in action at [https://ethtx.info/](https://ethtx.info/). Although `ctc` has its own transaction summarizing capabilities, it is currently much more limited than ethtx when it comes to tracing internal transactions and revealing the resultant state changes. These types of features may come to `ctc` in a future release.

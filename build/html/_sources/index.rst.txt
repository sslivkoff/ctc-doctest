.. note::
   :code:`ctc` is in beta, please report bugs to `the issue tracker <https://github.com/fei-protocol/checkthechain/issues>`_

   These docs are also a work in progress. Some sections are not yet complete. Feel free to report any documentation-related issues to the issue tracker.


Check the Chain (:code:`ctc`)
=============================

:code:`ctc` is a tool for historical data analysis of Ethereum and other EVM chains

It can be used as either 1) a cli tool or 2) a python package


Features
--------

.. hlist::
   :columns: 1

   * **data collection**: collects data from archive nodes robustly and efficiently
   * **data storage**: stores collected data on disk so that it only needs to be collected once
   * **data coding**: handles data encoding and decoding automatically by default
   * **data analysis**: computes derived metrics and other quantitative data summaries
   * **data visualization**: plots data to maximize data interpretability and sharing
   * **protocol specificity**: includes functionality for protocols like Chainlink and Uniswap
   * **command line interface**: performs many block explorer tasks in the terminal


Guide
-----

- To install ``ctc``, see `Installation <overview/installation.html>`_.
- To use ``ctc`` from the command line, see `Command Line Interface <cli/basic_usage.html>`_.
- To use ``ctc`` in python, see `Python Interface <python/code_tour.html>`_.
- To use ``ctc`` with specific protocols like Uniswap or Chainlink, see the `Specific Protocols (cli) <cli/subcommands/protocol.html>`_ or `Specific Protocols (python) <python/specific_protocols.html>`_.
- To view the ``ctc`` source code, check out the `GitHub Repository <https://github.com/fei-protocol/checkthechain>`_.


Datatypes
---------

.. list-table::
   :width: 65%
   :align: center
   :widths: 55 15 15 15
   :header-rows: 1

   * - Datatype
     - CLI
     - Python
     - Source
   * - ABIs
     - `CLI <cli/subcommands/data/abi.html>`__
     - `Python <python/datatypes/abis.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/evm/abi_utils>`__
   * - Addresses
     - `CLI <cli/subcommands/data/address.html>`__
     - `Python <python/datatypes/addresses.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/evm/address_utils>`__
   * - Binary Data
     - `CLI <cli/subcommands/compute.html>`__
     - `Python <python/datatypes/binary_data.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/evm/binary_utils>`__
   * - Blocks
     - `CLI <cli/subcommands/data/blocks.html>`__
     - `Python <python/datatypes/blocks.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/evm/block_utils>`__
   * - ERC20s
     - `CLI <cli/subcommands/data/erc20_balances.html>`__
     - `Python <python/datatypes/erc20s.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/evm/erc20_utils>`__
   * - ETH Balances
     - `CLI <cli/subcommands/data/eth_balances.html>`__
     - `Python <python/datatypes/eth_balances.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/evm/eth_utils>`__
   * - Events
     - `CLI <cli/subcommands/data/events.html>`__
     - `Python <python/datatypes/events.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/evm/event_utils>`__
   * - Transactions
     - `CLI <cli/subcommands/data/tx.html>`__
     - `Python <python/datatypes/transactions.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/evm/transaction_utils>`__


Specific Protocols
------------------

.. list-table::
   :width: 65%
   :align: center
   :widths: 55 15 15 15
   :header-rows: 1

   * - Protocol
     - CLI
     - Python
     - Source
   * - Aave V2
     - `CLI <cli/subcommands/protocol/aave.html>`__
     - `Python <python/protocols/aave_v2.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/aave_v2_utils/>`__
   * - Balancer
     - `CLI <cli/subcommands/data/dex_pools.html>`__
     - `Python <python/protocols/balancer.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/balancer_utils/>`__
   * - Chainlink
     - `CLI <cli/subcommands/protocol/chainlink.html>`__
     - `Python <python/protocols/chainlink.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/chainlink_utils>`__
   * - Compound
     - \-
     - `Python <python/protocols/compound.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/compound_utils/>`__
   * - Curve
     - `CLI <cli/subcommands/data/dex_pools.html>`__
     - `Python <python/protocols/curve.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/curve_utils/>`__
   * - ENS
     - `CLI <cli/subcommands/protocol/ens.html>`__
     - `Python <python/protocols/ens.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/ens_utils/>`__
   * - Fei
     - `CLI <cli/subcommands/protocol/fei_pcv.html>`__
     - `Python <python/protocols/fei.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/fei_utils/>`__
   * - Gnosis Safe
     - `CLI <cli/subcommands/protocol/gnosis.html>`__
     - `Python <python/protocols/gnosis_safe.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/gnosis_utils/>`__
   * - Multicall
     - `CLI <cli/subcommands/data/calls.html>`__
     - `Python <python/protocols/multicall.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/multicall_utils/>`__
   * - Rari
     - `CLI <cli/subcommands/protocol/rari.html>`__
     - `Python <python/protocols/rari.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/rari_utils/>`__
   * - Uniswap V2
     - `CLI <cli/subcommands/protocol/uniswap_chart.html>`__
     - `Python <python/protocols/uniswap_v2.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/uniswap_v2_utils/>`__
   * - Uniswap V3
     - `CLI <cli/subcommands/protocol/uniswap_chart.html>`__
     - `Python <python/protocols/uniswap_v3.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/uniswap_v3_utils/>`__
   * - Yearn
     - `CLI <cli/subcommands/protocol/yearn.html>`__
     - `Python <python/protocols/yearn.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/yearn_utils/>`__

External Data Sources
---------------------

.. list-table::
   :width: 65%
   :align: center
   :widths: 55 15 15 15
   :header-rows: 1

   * - Data Source
     - CLI
     - Python
     - Source
   * - 4byte
     - `CLI <cli/subcommands/protocol/4byte.html>`__
     - `Python <python/protocols/4byte.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/fourbyte_utils>`__
   * - CoinGecko
     - `CLI <cli/subcommands/protocol/cg.html>`__
     - `Python <python/protocols/coingecko.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/coingecko_utils>`__
   * - Defi Llama
     - `CLI <cli/subcommands/protocol/llama.html>`__
     - `Python <python/protocols/llama.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/llama_utils>`__
   * - Etherscan
     - `CLI <cli/subcommands/protocol/etherscan.html>`__
     - `Python <python/protocols/etherscan.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/etherscan_utils>`__

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: The Basics

   Introduction <self>

   ./overview/installation
   ./overview/dependencies
   ./overview/configuration
   ./overview/changelog
   ./overview/faq

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Data & Ops

   ./data_ops/obtaining_data
   ./data_ops/storing_data
   ./data_ops/performance
   ./data_ops/monitoring

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Command Line Interface

   ./cli/basic_usage
   ./cli/subcommands
   ./cli/useful_aliases
   ./cli/similar_tools

.. toctree::
   :maxdepth: 4
   :hidden:
   :caption: Python Interface

   ./python/code_tour
   ./python/rpc_client
   ./python/async_code
   ./python/datatypes
   ./python/specific_protocols
   ./python/similar_tools

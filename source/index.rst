.. note::
   :code:`ctc` is in beta, please report bugs to `the issue tracker <https://github.com/fei-protocol/checkthechain>`_


Check the Chain (:code:`ctc`)
=============================

:code:`ctc` is a tool for historical data analysis of Ethereum and other EVM chains

It can be used as either 1) a python package or 2) a cli tool


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
- To see examples of what you can do with ``ctc``, see `Case Studies <case_studies/under_construction.html>`_.


Datatypes
---------

.. list-table::
   :width: 55%
   :align: center
   :widths: 55 15 15
   :header-rows: 1

   * - Datatype
     - CLI Docs
     - Python Docs
   * - ABIs
     - `CLI Docs <cli/subcommands/data/abi.html>`__
     - `Python Docs <python/datatypes/abis.html>`__
   * - Binary Data
     - `CLI Docs <cli/subcommands/compute.html>`__
     - `Python Docs <python/datatypes/binary_data.html>`__
   * - Blocks
     - `CLI Docs <cli/subcommands/data/blocks.html>`__
     - `Python Docs <python/datatypes/blocks.html>`__
   * - Contracts
     - `CLI Docs <cli/subcommands/data/address.html>`__
     - `Python Docs <python/datatypes/contracts.html>`__
   * - Gas
     - `CLI Docs <cli/subcommands/data/gas.html>`__
     - `Python Docs <python/datatypes/gas.html>`__
   * - ERC20s
     - `CLI Docs <cli/subcommands/data/erc20_balances.html>`__
     - `Python Docs <python/datatypes/erc20s.html>`__
   * - ETH Balances
     - `CLI Docs <cli/subcommands/data/eth_balances.html>`__
     - `Python Docs <python/datatypes/eth_balances.html>`__
   * - Events
     - `CLI Docs <cli/subcommands/data/events.html>`__
     - `Python Docs <python/datatypes/events.html>`__
   * - Transactions
     - `CLI Docs <cli/subcommands/data/transaction.html>`__
     - `Python Docs <python/datatypes/transactions.html>`__


Specific Protocols
------------------

.. list-table::
   :width: 65%
   :align: center
   :widths: 55 15 15 15
   :header-rows: 1

   * - Protocol
     - CLI Docs
     - Python Docs
     - Source
   * - Aave V2
     - CLI Docs
     - `Python Docs <python/protocols/aave_v2.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/aave_v2_utils/>`__
   * - Balancer
     - CLI Docs
     - `Python Docs <python/protocols/balancer.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/balancer_utils/>`__
   * - Chainlink
     - CLI Docs
     - `Python Docs <python/protocols/chainlink.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/chainlink_utils>`__
   * - Compound
     - CLI Docs
     - `Python Docs <python/protocols/compound.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/compound_utils/>`__
   * - Curve
     - CLI Docs
     - `Python Docs <python/protocols/curve.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/curve_utils/>`__
   * - ENS
     - CLI Docs
     - `Python Docs <python/protocols/ens.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/ens_utils/>`__
   * - Fei
     - CLI Docs
     - `Python Docs <python/protocols/fei.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/fei_utils/>`__
   * - Rari
     - CLI Docs
     - `Python Docs <python/protocols/rari.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/rari_utils/>`__
   * - Uniswap V2
     - CLI Docs
     - `Python Docs <python/protocols/uniswap_v2.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/uniswap_v2_utils/>`__
   * - Uniswap V3
     - CLI Docs
     - `Python Docs <python/protocols/uniswap_v3.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/uniswap_v3_utils/>`__

External Data Sources
---------------------

.. list-table::
   :width: 65%
   :align: center
   :widths: 55 15 15 15
   :header-rows: 1

   * - Data Source
     - CLI Docs
     - Python Docs
     - Source
   * - 4byte
     - `CLI Docs <cli/subcommands/protocol/4byte.html>`__
     - `Python Docs <python/protocols/4byte.html>`__
     - `Source <https://github.com/fei-protocol/checkthechain/tree/main/src/ctc/protocols/fourbyte_utils>`__
   * - CoinGecko
     - `CLI Docs <cli/subcommands/protocol/cg.html>`__
     - \-
     - `Source <https://github.com/fei-protocol/checkthechain/blob/main/src/ctc/cli/commands/data/cg_command.py>`__
   * - Etherscan
     - \-
     - \-
     - `Source <https://github.com/fei-protocol/checkthechain/blob/main/src/ctc/evm/abi_utils/abi_io/contract_abi_backends/etherscan_contract_abis.py>`__

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: The Basics

   Introduction <self>

   ./overview/installation
   ./overview/dependencies
   ./overview/configuration
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

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Case Studies

   ./case_studies/under_construction


.. other case studies
    gas monitoring
    crypto market state


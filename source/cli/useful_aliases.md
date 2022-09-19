

# Useful Aliases

`ctc` makes it simple to perform many tasks from the command line. However, `ctc` can be made even more simple by using shell aliases that reduce the number of required keystrokes that must be typed. The `ctc` codebase includes an optional set of cli aliases for this purpose.

Such aliases make it so you do not need to type the "ctc" before a subcommand name. For example, instead of typing `ctc keccak <address>`, you just type `keccak <address>`. Instead of typing `ctc 4byte <query>`, you just type `4byte <query>`. And so on, for many different `ctc` subcommands.

The `ctc setup` wizard can add these aliases to your shell configuation.

## The Aliases

These aliases are chosen so as not to conflict with any common CLI tools.

```bash
# compute commands
alias ascii="ctc ascii"
alias hex="ctc hex"
alias keccak="ctc keccak"
alias lower="ctc lower"

# data commands
alias abi="ctc abi"
alias address="ctc address"
alias block="ctc block"
alias blocks="ctc blocks"
alias bytecode="ctc bytecode"
alias call="ctc call"
alias calls="ctc calls"
alias dex="ctc dex"
alias erc20="ctc erc20"
alias eth="ctc eth"
alias gas="ctc gas"
alias int="ctc int"
alias rlp="ctc rlp"
alias tx="ctc tx"

# protocol commands
alias 4byte="ctc 4byte"
alias aave="ctc aave"
alias cg="ctc cg"
alias chainlink="ctc chainlink"
alias curve="ctc curve"
alias es="ctc etherscan"
alias ens="ctc ens"
alias fei="ctc fei"
alias gnosis="ctc gnosis"
alias llama="ctc llama"
alias rari="ctc rari"
alias uniswap="ctc uniswap"
alias yearn="ctc yearn"
```

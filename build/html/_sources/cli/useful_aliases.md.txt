
# Useful Aliases

`ctc` makes it simple to perform many tasks from the command line. However, `ctc` can be made even more simple by using shell aliases that reduce the number of required keystrokes that must be typed.

The `ctc` codebase includes an optional set of cli aliases for this purpose. These aliases can be found in [a script](https://github.com/fei-protocol/checkthechain/blob/main/scripts/ctc_aliases.sh) in the repo, but they are also pasted below for convenience.

These aliases make it so you do not need to type the `"ctc"` before a subcommand name. For example, instead of typing `ctc keccak <address>`, you just type `keccak <address>`. Instead of typing `ctc 4byte <query>`, you just type `4byte <query>`. And so on, for many different `ctc` subcommands.

To use these aliases, you need to include them in your shell config file (e.g. `~/.profile`). You can either copy paste the alias commands directly, or you can add a single line: `source <PATH_TO_ALIAS_FILE>`.

## The Aliases File

```bash
#!/bin/sh

# these commands allow you to call ctc subcommands without typing the "ctc" part

# to use, either:
# 1. add the contents of this file to the end of your terminal config file
# 2. add `source PATH_TO_THIS_FILE` to the end of your terminal config file

# to learn more about these commands, run `ctc help`

# depending on preference can use all of these aliases or just a subset of them:

# compute commands
alias ascii="ctc ascii"
alias hex="ctc hex"
alias keccak="ctc keccack"
alias lower="ctc lower"

# data commands
alias address="ctc address"
alias block="ctc block"
alias blocks="ctc blocks"
alias call="ctc call"
alias calls="ctc calls"
alias eth="ctc eth"
alias erc20="ctc erc20"
alias transaction="ctc transaction"
alias gas="ctc gas"

# protocol commands
alias 4byte="ctc 4byte"
alias cg="ctc coingecko"
alias chainlink="ctc chainlink"
alias curve="ctc curve"
alias ens="ctc ens"
alias fei="ctc fei"
alias rari="ctc rari"
```


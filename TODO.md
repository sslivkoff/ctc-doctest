
## TODO

- do a high level overview of what highlevel org changes should happen
    - make a list, add to todo
- do a readthrough of all copy, see what needs to change
    - make a list, add to todo
- update README
    - add to the docs readme for steps of how to develop and build the docs
- add note about environment variables, including ETH_RPC_NODE or whatever it's called
- specific points
    - in Introduction update list of datatype, protocols, and external data sources
- add note about new api to readme

## Done
- fix help urls in ctc -h
- get a doc generation run working
- Overview section
    - Installation
        - add note about installing from git commits
    - Dependencies
        - rewrite the libraries section
        - add note about strict mode type checking
    - create a Changelog page



## TODO After 0.3.0


## Rough Plan
- go through old notes on meeting with rari where talked about ctc on high level
- look at docs of other projects for inspiration
    - https://web3py.readthedocs.io/en/stable/

## Url
- make docs take the URL `checkthechain.github.io/docs`
    - can do this one of two ways
        - make as repo named `checkthechain.github.io`, put docs stuff in `/docs` folder
        - make repo named `docs`
- eventually transfer this to `ctc.xyz`

## Resources
- sphinx
    - getting started https://www.sphinx-doc.org/en/master/usage/quickstart.html
    - directives https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#toctree-directive
- readthedocs theme https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
- myst markdown parser
    - https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html
- rst
    - https://docutils.sourceforge.io/docs/user/rst/quickref.html
- blog posts
    - https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/

# Modifying the theme
- https://stackoverflow.com/questions/23211695/modifying-content-width-of-the-sphinx-theme-read-the-docs
- dark mode
    - not 1st class feature, but see:
    - https://github.com/readthedocs/readthedocs.org/issues/3819
    - https://github.com/readthedocs/sphinx_rtd_theme/issues/224#issuecomment-722655021
    - https://github.com/python-pillow/Pillow/pull/4968
    - https://github.com/MrDogeBro/sphinx_rtd_dark_mode
    - sphinx rtd examples
        - https://docs.godotengine.org/en/stable/index.html
        - https://pillow.readthedocs.io/en/stable/installation.html
- modifying sidebar width
    - https://stackoverflow.com/questions/23211695/modifying-content-width-of-the-sphinx-theme-read-the-docs


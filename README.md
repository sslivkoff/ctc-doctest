
# ctc docs

These are the source files used to generate the ctc docs.

View the generated docs at https://checkthechain.github.io/docs

## Building

```bash
make clean html
```

autobuild after changes
```bash
sphinx-autobuild source build/html
```

## Dependencies
```
pip install ctc
pip install sphinx
pip install myst-parser
pip install sphinx-autobuild
pip install sphinx-rtd-theme
pip install sphinx-copybutton
```


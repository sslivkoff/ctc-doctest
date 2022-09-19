
# ctc docs

These are the source files used to generate the ctc docs.

View the generated docs at https://checkthechain.github.io/docs

## Building

In repo root run:
```bash
BUILDING_SPHINX=1 ./generate_all
```

This command generates many html files and then runs the standard sphinx build pipeline.

Once the html is generated, the sphinx pipeline can be run in its own using:

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
